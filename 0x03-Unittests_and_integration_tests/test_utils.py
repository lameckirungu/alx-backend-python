#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest  
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json

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
        
class TestGetJson(unittest.TestCase):
    """
    Tests `utils.get_json` function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    
    def test_get_json(self, test_url, expected_payload):
        """
        Tests that utils.get_json returns the expected payload 
        without making real HTTP calls.
        """
        with patch('utils.requests.get') as mocked_get:
            mock_response = Mock()
            mock_response.json.return_value = expected_payload
            mocked_get.return_value = mock_response
            
            result = get_json(test_url)
            self.assertEqual(result, expected_payload)
            mocked_get.assert_called_once_with(test_url)
