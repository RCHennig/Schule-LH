class PageNode:
    def __init__(self, node_id):
        # Initialisierung der PageNode mit einer eindeutigen ID, leeren Listen für ausgehende und eingehende Links, und einem initialen PageRank-Wert von 1.0
        self.id = node_id
        self.outgoing_links = []  # Liste für ausgehende Links von dieser Seite
        self.incoming_links = []  # Liste für eingehende Links zu dieser Seite
        self.pagerank = 1.0  # Initialer PageRank-Wert

    def get_id(self):
        # Rückgabe der ID dieser Seite
        return self.id

    def get_outgoing_links(self):
        # Rückgabe der Liste ausgehender Links von dieser Seite
        return self.outgoing_links

    def get_incoming_links(self):
        # Rückgabe der Liste eingehender Links zu dieser Seite
        return self.incoming_links

    def get_pagerank(self):
        # Rückgabe des aktuellen PageRank-Werts dieser Seite
        return self.pagerank

    def set_pagerank(self, value):
        # Setzen des PageRank-Werts dieser Seite auf den übergebenen Wert
        self.pagerank = value


class PageRankGraph:
    def __init__(self):
        # Initialisierung des PageRankGraph mit einer leeren Liste für PageNode-Objekte
        self.nodes = []

    def add_node(self, node):
        # Hinzufügen eines PageNode-Objekts zur Liste im Graphen
        self.nodes.append(node)

    def get_nodes(self):
        # Rückgabe der Liste aller PageNode-Objekte im Graphen
        return self.nodes

    def calculate_pagerank(self, num_iterations, damping_factor=0.85):
        # Iterative Berechnung des PageRanks für den Graphen
        for _ in range(num_iterations):
            new_pageranks = []

            # Berechnung der neuen PageRanks für jeden PageNode im Graphen
            for node in self.nodes:
                new_pagerank = (1 - damping_factor) + damping_factor * sum(
                    incoming_node.get_pagerank() / len(incoming_node.get_outgoing_links())
                    for incoming_node in node.get_incoming_links()
                )
                new_pageranks.append(new_pagerank)

            # Aktualisierung der PageRanks der PageNode-Objekte im Graphen
            for i, node in enumerate(self.nodes):
                node.set_pagerank(new_pageranks[i])


#Nutzung
node_a = PageNode(1)
node_b = PageNode(2)
node_c = PageNode(3)

# Setzen der ausgehenden und eingehenden Links zwischen den Seiten im Beispiel-Graphen
node_a.outgoing_links = [node_b, node_c]
node_a.incoming_links = [node_b]
node_b.outgoing_links = [node_c, node_a]
node_b.incoming_links = [node_a]
node_c.incoming_links = [node_b, node_a]

graph = PageRankGraph()
graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)

graph.calculate_pagerank(num_iterations=10)

# Ausgabe der berechneten PageRanks für jede Seite im Graphen
for node in graph.get_nodes():
    print(f"Page {node.get_id()}: PageRank = {node.get_pagerank()}")

import unittest

class PageRankTest(unittest.TestCase):
    def setUp(self):
        # Erstelle Testgraph
        self.node_a = PageNode(1)
        self.node_b = PageNode(2)
        self.node_c = PageNode(3)

        # Setze Links im Testgraphen
        self.node_a.outgoing_links = [node_b, node_c]
        self.node_a.incoming_links = [node_b]
        self.node_b.outgoing_links = [node_c, node_a]
        self.node_b.incoming_links = [node_a]
        self.node_c.incoming_links = [node_b, node_a]

        # Erstelle PageRankGraph und füge Nodes hinzu
        self.graph = PageRankGraph()
        self.graph.add_node(self.node_a)
        self.graph.add_node(self.node_b)
        self.graph.add_node(self.node_c)

    def test_pagerank_calculation(self):
        # Berechne PageRanks
        self.graph.calculate_pagerank(num_iterations=10)

        # Überprüfe die berechneten Werte mit den händisch berechneten Werten
        expected_pageranks = {1: 0.2610, 2: 0.2610, 3: 0.3720}
        for node in self.graph.get_nodes():
            expected_pagerank = expected_pageranks[node.get_id()]
            actual_pagerank = node.get_pagerank()

            # Verwende assertAlmostEqual für Genauigkeit mit Rundungsfehler
            self.assertAlmostEqual(actual_pagerank, expected_pagerank, places=3)

if __name__ == '__main__':
    unittest.main()
