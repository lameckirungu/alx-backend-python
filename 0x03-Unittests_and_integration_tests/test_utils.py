#!/usr/bin/env python3
"""Unit tests for utils.py"""
from parameterized import parameterized
import unittest
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """Tests `utils.access_nested_map` function."""
        
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])   
    
    def test_access_nested_map(self, nested_map, path, expected):
        """Tests access_nested_map returns correct value."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests access_nested_map raises KeyError for invalid path with correct message.
        
        :param self: The test case instance.
        :param nested_map: the nested map
        :param path: the path
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")
        