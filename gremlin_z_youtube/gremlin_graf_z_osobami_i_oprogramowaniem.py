from gremlin_test_polaczenia_z_serwerem import *

from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import GraphTraversal, GraphTraversalSource

from gremlin_python.process.traversal import T

def get_vertex_types(g: GraphTraversalSource) -> list:
    return g.V().label().groupCount().toList()

def get_edge_types(g: GraphTraversalSource) -> list:
    return g.E().label().groupCount().toList()

if __name__ == '__main__':
    logger = get_logger()

    connection = create_graph_server_connection()
    g = create_graph_traversal(connection, logger)

    drop_all_vertices(g)

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

    show_info_about_graph(g, logger)

    # filtrowanie grafu
    # wierzchołki
    vertex_types: list = get_vertex_types(g)
    for key, value in vertex_types[0].items():
        print(f'vertex label : {key}, occurences : {value}')
    # gałęzie
    edge_types: list = get_edge_types(g)
    for key, value in edge_types[0].items():
        print(f'edge label : {key}, occurences : {value}')

    connection.close()