#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Tuple
from utils import access_nested_map


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
        """Test access_nested_map returns correct value for given path."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
