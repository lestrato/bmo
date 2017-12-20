#!/usr/bin/env python
"""Ensures the correctness of graph_utils.py, part_1.py, part_2.py, part_3.py


"""
import graph_utils
import errors
from part_1 import route_distance
from part_2 import get_num_bfs_paths, get_bfs_paths
from part_3 import dijkstra

import unittest

# === graph_utils.py ===
class TestGraphUtilMethods(unittest.TestCase):
    def setUp(self):
        self.edges = [
            ("A", "B", 5),
            ("B", "C", 4),
            ("C", "D", 8),
            ("D", "C", 8),
            ("D", "E", 6),
            ("A", "D", 5),
            ("C", "E", 2),
            ("E", "B", 3),
            ("A", "E", 7),
        ]

    def test_bad_edge_costs_1(self):
        with self.assertRaises(errors.BadEdgeCostError) as context:
            edges = [
                ("A", "B", 5),
                ("B", "C", -3),
            ]
            graph_utils.make_graph(edges)

        self.assertTrue('must be an integer' in str(context.exception))

    def test_bad_edge_costs_2(self):
        with self.assertRaises(errors.BadEdgeCostError) as context:
            edges = [
                ("A", "B", 5),
                ("B", "C", 4.3),
            ]
            graph_utils.make_graph(edges)

        self.assertTrue('must be an integer' in str(context.exception))

    def test_good_edge_costs_1(self):
        from collections import defaultdict
        edges = [
            ("A", "B", 5),
            ("B", "C", 43),
        ]
        graph = graph_utils.make_graph(edges)

        self.assertTrue(type(graph) == defaultdict)

    def test_good_edge_file_1(self):
        file = 'test_files/good_edge_file_1.txt'
        edges = graph_utils.file_to_edgeset(file)

        self.assertEqual(edges, self.edges)

    def test_good_edge_file_2(self):
        file = 'test_files/good_edge_file_2.txt'
        edges = graph_utils.file_to_edgeset(file)

        self.assertEqual(edges, 
            [
                ("A", "B", 5),
                ("B", "C", 43),
            ]
        )

    def test_bad_edge_file_1(self):
        file = 'test_files/bad_edge_file_1.txt'

        with self.assertRaises(errors.BadFileContentsError) as context:
            edges = graph_utils.file_to_edgeset(file)

        self.assertTrue('first letter' in str(context.exception))

    def test_bad_edge_file_2(self):
        file = 'test_files/bad_edge_file_2.txt'

        with self.assertRaises(errors.BadFileContentsError) as context:
            edges = graph_utils.file_to_edgeset(file)

        self.assertTrue('second letter' in str(context.exception))

    def test_bad_edge_file_3(self):
        file = 'test_files/bad_edge_file_3.txt'

        with self.assertRaises(errors.BadFileContentsError) as context:
            edges = graph_utils.file_to_edgeset(file)

        self.assertTrue('interpret line' in str(context.exception))

    def test_bad_edge_file_4(self):
        file = 'test_files/bad_edge_file_4.txt'

        with self.assertRaises(errors.BadFileContentsError) as context:
            edges = graph_utils.file_to_edgeset(file)

        self.assertTrue('edge weight' in str(context.exception))

    def test_bad_edge_file_6(self):
        file = 'test_files/bad_edge_file_6.txt'

        with self.assertRaises(errors.BadFileContentsError) as context:
            edges = graph_utils.file_to_edgeset(file)

        self.assertTrue('already exists in the edge set' in str(context.exception))

# === part_1.py ===
class TestPart1Methods(unittest.TestCase):
    def setUp(self):
        edges = [
            ("A", "B", 5),
            ("B", "C", 4),
            ("C", "D", 8),
            ("D", "C", 8),
            ("D", "E", 6),
            ("A", "D", 5),
            ("C", "E", 2),
            ("E", "B", 3),
            ("A", "E", 7),
        ]

        self.graph = graph_utils.make_graph(edges)

    def test_vertex_doesnt_exist_in_graph(self):
        with self.assertRaises(errors.DoesNotExistError) as context:
            route_distance(self.graph, 'ABZ')

        self.assertTrue('does not exist as a connected vertex in the graph' in str(context.exception))

    def test_valid_route_1(self):
        total_cost = route_distance(self.graph, 'ABC')

        self.assertEqual(total_cost, 9)

    def test_valid_route_2(self):
        total_cost = route_distance(self.graph, 'AD')

        self.assertEqual(total_cost, 5)

    def test_valid_route_3(self):
        total_cost = route_distance(self.graph, 'ADC')

        self.assertEqual(total_cost, 13)

    def test_valid_route_4(self):
        total_cost = route_distance(self.graph, 'AEBCD')

        self.assertEqual(total_cost, 22)

    def test_invalid_route_1(self):
        total_cost = route_distance(self.graph, 'AED')

        self.assertEqual(total_cost, 'NO SUCH ROUTE')

# === part_2.py ===
class TestPart2Methods(unittest.TestCase):
    def setUp(self):
        edges = [
            ("A", "B", 5),
            ("B", "C", 4),
            ("C", "D", 8),
            ("D", "C", 8),
            ("D", "E", 6),
            ("A", "D", 5),
            ("C", "E", 2),
            ("E", "B", 3),
            ("A", "E", 7),
        ]

        self.graph = graph_utils.make_graph(edges)

    def test_source_vertex_doesnt_exist_in_graph(self):
        with self.assertRaises(errors.DoesNotExistError) as context:
            get_num_bfs_paths(self.graph, 'A', 'ARF', 'towns', 'less_than', 3)

        self.assertTrue('does not exist as a connected vertex in the graph' in str(context.exception))

    def test_dest_vertex_doesnt_exist_in_graph(self):
        with self.assertRaises(errors.DoesNotExistError) as context:
            get_num_bfs_paths(self.graph, 'FEAR', 'C', 'towns', 'less_than', 3)

        self.assertTrue('does not exist as a connected vertex in the graph' in str(context.exception))

    def test_bad_filter_type(self):
        with self.assertRaises(ValueError) as context:
            get_num_bfs_paths(self.graph, 'A', 'C', 'grass', 'less_than', 3)

        self.assertTrue('accepted filter types are' in str(context.exception))

    def test_bad_operator(self):
        with self.assertRaises(ValueError) as context:
            get_num_bfs_paths(self.graph, 'A', 'C', 'towns', 'smells_like', 3)

        self.assertTrue('accepted operators are' in str(context.exception))

    def test_bad_value_float(self):
        with self.assertRaises(ValueError) as context:
            get_num_bfs_paths(self.graph, 'A', 'C', 'towns', 'equal_to', 3.3)

        self.assertTrue('must be an integer' in str(context.exception))

    def test_bad_value_neg_int(self):
        with self.assertRaises(ValueError) as context:
            get_num_bfs_paths(self.graph, 'A', 'C', 'towns', 'equal_to', -3)

        self.assertTrue('must be an integer' in str(context.exception))

    def test_less_than_stops(self):
        number_of_trips = get_num_bfs_paths(self.graph, 'C', 'C', 'towns', 'less_than', 4)

        self.assertEqual(number_of_trips, 2)

    def test_more_than_stops(self):
        number_of_trips = get_num_bfs_paths(self.graph, 'A', 'C', 'towns', 'more_than', 4)

        self.assertEqual(number_of_trips, 0)

    def test_equal_to_stops(self):
        number_of_trips = get_num_bfs_paths(self.graph, 'B', 'B', 'towns', 'equal_to', 3)

        self.assertEqual(number_of_trips, 1)

    def test_less_than_distance(self):
        number_of_trips = get_num_bfs_paths(self.graph, 'A', 'B', 'distance', 'less_than', 15)

        self.assertEqual(number_of_trips, 3)

    def test_more_than_distance(self):
        number_of_trips = get_num_bfs_paths(self.graph, 'A', 'C', 'distance', 'more_than', 10)

        self.assertEqual(number_of_trips, 3)

    def test_equal_to_distance(self):
        number_of_trips = get_num_bfs_paths(self.graph, 'B', 'B', 'distance', 'equal_to', 9)

        self.assertEqual(number_of_trips, 1)

    def test_paths_same_vertex(self):
        paths = get_bfs_paths(self.graph, 'B', 'B')

        self.assertEqual(paths, set([(('B', 'C', 'E', 'B'), 9), (('B', 'C', 'D', 'E', 'B'), 21)]))

    def test_paths_diff_vertex_1(self):
        paths = get_bfs_paths(self.graph, 'B', 'D')

        self.assertEqual(paths, set([(('B', 'C', 'D'), 12)]))

    def test_paths_diff_vertex_2(self):
        paths = get_bfs_paths(self.graph, 'E', 'B')

        self.assertEqual(paths, set([(('E', 'B'), 3)]))

# === part_3.py ===
class TestPart3Methods(unittest.TestCase):
    def setUp(self):
        edges = [
            ("A", "B", 5),
            ("B", "C", 4),
            ("C", "D", 8),
            ("D", "C", 8),
            ("D", "E", 6),
            ("A", "D", 5),
            ("C", "E", 2),
            ("E", "B", 3),
            ("A", "E", 7),
        ]

        self.graph = graph_utils.make_graph(edges)

    def test_source_vertex_doesnt_exist_in_graph(self):
        with self.assertRaises(errors.DoesNotExistError) as context:
            dijkstra(self.graph, 'A', 'ARF')

        self.assertTrue('does not exist as a connected vertex in the graph' in str(context.exception))

    def test_dest_vertex_doesnt_exist_in_graph(self):
        with self.assertRaises(errors.DoesNotExistError) as context:
            dijkstra(self.graph, 'FEAR', 'C')

        self.assertTrue('does not exist as a connected vertex in the graph' in str(context.exception))

    def test_route_doesnt_exist(self):
        route = dijkstra(self.graph, 'D', 'A')

        self.assertEqual(route, 'NO SUCH ROUTE')

    def test_route_correct_cost_1(self):
        route, cost = dijkstra(self.graph, 'A', 'C')

        self.assertEqual(cost, 9)

    def test_route_correct_cost_2(self):
        route, cost = dijkstra(self.graph, 'B', 'B')

        self.assertEqual(cost, 9)

    def test_route_correct_route_1(self):
        route, cost = dijkstra(self.graph, 'A', 'C')

        self.assertEqual(route, ['A', 'B', 'C'])

    def test_route_correct_route_2(self):
        route, cost = dijkstra(self.graph, 'B', 'B')

        self.assertEqual(route, ['B', 'C', 'E', 'B'])

if __name__ == '__main__':
    unittest.main()
