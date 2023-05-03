from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import GraphTraversal, GraphTraversalSource

import logging
from logging import Logger

def get_logger() -> Logger:
    logging.basicConfig(level = logging.INFO)
    return logging.getLogger(name = 'GREMLIN_TEST_POLACZENIA_Z_SERWEREM')

def create_graph_server_connection() -> DriverRemoteConnection:
    return DriverRemoteConnection('ws://localhost:8182/gremlin','g')

def create_graph_traversal(connection, logger: Logger) -> GraphTraversalSource:
    graph_traversal = traversal().withRemote(connection)
    logger.info('Utworzono połączenie z serwerem Gremlina')
    return graph_traversal

def drop_all_vertices(g: GraphTraversalSource) -> None:
    g.V().drop().iterate()

def create_vertex(g: GraphTraversalSource, logger: Logger, label: str, vertex_properties: dict) -> GraphTraversal:
    new_vertex = g.addV(label)
    for key, value in vertex_properties.items():
        new_vertex = new_vertex.property(key, value)
    logger.info('Utworzono wierzchołek w grafie')
    return new_vertex.next()

def create_edge(g: GraphTraversalSource, logger: Logger, v1: GraphTraversal, v2: GraphTraversal) -> GraphTraversal:
    edge = g.V(v1).addE('knows').to(v2).property('weight', 0.75).iterate()
    logger.info('Utworzono gałąź w grafie')
    return edge

def show_info_about_graph(g: GraphTraversalSource, logger: Logger):
    logger.info(f'Informacje na temat grafu (wierzchołki) :{g.V().toList()}')
    logger.info(f'Informacje na temat grafu (gałęzie) :{g.E().toList()}')

    for vertex in g.V().toList():
        print(f'vertex properties : {g.V(vertex).properties().toList()}')
    
    for vertex in g.V().toList():
        print(f'vertex value map : {g.V(vertex).valueMap().next()}')

    # marko = g.V().has('person','name','marko').next()
    # logger.info(f'Pobrano węzęł : {marko["name"]}')
    # print(marko)

    # peopleMarkoKnows = g.V().has('person','name','marko').out('knows').toList()
    # logger.info(f'Pobrano listę znajowmych węzła {marko["name"]} o długości {len(peopleMarkoKnows)}')
    # print(peopleMarkoKnows)

if __name__ == '__main__':
    logger = get_logger()
    connection = create_graph_server_connection()
    g = create_graph_traversal(connection, logger)
    drop_all_vertices(g)
    v1_properties = {'id' : 1, 'label' : 'person', 'name' : 'marko', 'age' : '32', 'languages' : ['PHP', 'PERL']}
    v1 = create_vertex(g, logger, 'person', v1_properties)
    v2_properties = {'id' : 2, 'label' : 'person', 'name' : 'stephen', 'age' : '25', 'languages' : ['.NET', 'C++']}
    v2 = create_vertex(g, logger, 'person', v2_properties)
    edge = create_edge(g, logger, v1, v2)
    show_info_about_graph(g, logger)
    connection.close()