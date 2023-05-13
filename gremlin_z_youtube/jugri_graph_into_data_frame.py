
import pandas as pd
# import jugri
from gremlin_python.structure.graph import Element, Path
from gremlin_python.process.graph_traversal import GraphTraversal, GraphTraversalSource
#import collections
from collections.abc import MutableMapping

from gremlin_test_polaczenia_z_serwerem import *

class GraphIntoDataFrame:
    
    def __init__(self, graph_traversal: GraphTraversal):
        self.graph_traversal = graph_traversal

    # def convert_graph_into_data_frame(self) -> pd.DataFrame:
    #     """ ta metoda wykorzystuje moduł JUGRI """
    #     data_frame: pd.DataFrame = jugri.to_df(self.graph_traversal)
    #     return data_frame

    def custom_convert_graph_into_data_frame(self) -> pd.DataFrame:
        """ 
        ta metoda korzysta z implementacji modułu JUGRI - copy / paste 
        
        Converts a Gremlin Traversal to a Pandas DataFrame. It expects a traversal or a list of traversal results.
        :param gremlin_traversal: A gremlinpython graph traversal (e.g. g.V().limit(5)) or a list (e.g. g.V().limit(5).toList())
        """

        gremlin_traversal: GraphTraversal = self.graph_traversal

        if type(gremlin_traversal) is GraphTraversal:
            gremlin_traversal = gremlin_traversal.toList()
        if len(gremlin_traversal) == 0:
            return pd.DataFrame()

        if type(gremlin_traversal[0]) is dict:
            if "@type" in gremlin_traversal[0].keys() and gremlin_traversal[0]["@type"] == "g:TraversalMetrics":
                df = pd.DataFrame([self.flatten(_["@value"], sep='.') for _ in gremlin_traversal[0]["@value"]["metrics"]])
            else:
                gremlin_traversal = [self.flatten(_, sep='.') for _ in gremlin_traversal]
                df = pd.DataFrame(gremlin_traversal)
        elif isinstance(gremlin_traversal[0], Element):
            df = pd.DataFrame([_.__dict__ for _ in gremlin_traversal])
        elif type(gremlin_traversal[0]) is Path:
            df = pd.DataFrame([dict(enumerate(_)) for _ in gremlin_traversal])
        else:
            df = pd.DataFrame(gremlin_traversal)
        return df.applymap(self.get_singular)
    
    def get_singular(self, value):
        if type(value) is list:
            lv = len(value)
            if lv == 1:
                return value[0]
            elif lv == 0:
                None
            else:
                return value
        else:
            return value

    def flatten(self, d, parent_key='', sep='_'):
        """
        Flatten nested fields using recursive calls.
        :param d: dictionary
        :param parent_key: current key
        :param sep: key separator
        :return: flattened dictionary
        """
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + str(k) if parent_key else k
            if isinstance(v, MutableMapping):
                items.extend(self.flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

# testy klasy GraphIntoDataFrame
if __name__ == '__main__':
    logger = get_logger()

    connection = create_graph_server_connection()
    g = create_graph_traversal(connection, logger)

    # drop_all_vertices(g)

    # wierzchołki grafu
    # osoby
    vertex_properties = {'name' : 'marko', 'age' : '29'}
    vertex_marko = create_vertex(g, logger, 'person', vertex_properties)
    vertex_properties = {'name' : 'vadas', 'age' : '27'}
    vertex_vadas = create_vertex(g, logger, 'person', vertex_properties)
    vertex_properties = {'name' : 'josh', 'age' : '32'}
    vertex_josh = create_vertex(g, logger, 'person', vertex_properties)
    vertex_properties = {'name' : 'peter', 'age' : '35'}
    vertex_peter = create_vertex(g, logger, 'person', vertex_properties)
    # oprogramowanie
    vertex_properties = {'name' : 'lop', 'lang' : 'java'}
    vertex_lop = create_vertex(g, logger, 'software', vertex_properties)
    vertex_properties = {'name' : 'ripple', 'lang' : 'java'}
    vertex_ripple = create_vertex(g, logger, 'software', vertex_properties)

    # krawędzie grafu
    create_edge(g, logger, vertex_marko, vertex_vadas, 'knows', {'weight' : '0.5'})
    create_edge(g, logger, vertex_marko, vertex_josh, 'knows', {'weight' : '1.0'})
    create_edge(g, logger, vertex_marko, vertex_lop, 'created', {'weight' : '0.4'})
    create_edge(g, logger, vertex_josh, vertex_lop, 'created', {'weight' : '0.4'})
    create_edge(g, logger, vertex_josh, vertex_ripple, 'created', {'weight' : '1.0'})
    create_edge(g, logger, vertex_peter, vertex_lop, 'created', {'weight' : '0.2'})

    # show_info_about_graph(g, logger)

    graph_traversal: GraphTraversal = g.V().elementMap()
    graph_converter = GraphIntoDataFrame(graph_traversal)

    # print(f'Graph traversal :  {g.V().hasLabel("person").valueMap(True).toList()}')
    # print(f'Graph traversal :  {g.V().hasLabel("person").elementMap()}')

    data_frame: pd.DataFrame = graph_converter.custom_convert_graph_into_data_frame()

    # z jakimi trawersami działa JUGRI :
    #   g.V(), g.E(), g.V().id(), g.V().id_(), g.V().label(), ..
    #   g.V().hasLabel('person'), g.E().hasLabel('created'), ..
    #   g.V().hasLabel('person').properties(), g.V().hasLabel('person', 'software').properties()
    #   g.V().hasLabel('person').elementMap(), g.V().hasLabel('software').elementMap()
    #   g.V().elementMap() - wartosci NaN jezeli kolumna nie jest zdefiniowana

    # data_frame: pd.DataFrame = graph_converter.convert_graph_into_data_frame()
    
    print(f'Wygenerowany z grafu obiekt Pandas Data Frame : {data_frame}')

    drop_all_vertices(g)

    connection.close()
