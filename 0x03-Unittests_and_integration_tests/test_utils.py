#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Tuple, Dict
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """TestCase for the access_nested_map utility function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping[str, Any],
                               path: Sequence[str],
                               expected: Any) -> None:
        # """Test access_nested_map returns correct value for given path."""
        # self.assertEqual(access_nested_map(nested_map, path), expected)
        """Test access_nested_map raises KeyError with invalid path."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """TestCase for the get_json utility function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict[str, Any],
                      mock_get: Mock) -> None:
        """Test get_json returns correct JSON from mocked GET request."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)
