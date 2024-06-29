#!/usr/bin/env python3
"""Module for testing the functions in the utils file"""
import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Unittest for access_nested_map class/function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected: Union[Dict, int]) -> None:
        """Tests for function output: access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception) -> None:
        """Tests for exception raising: access_nested_map"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Unittest for get_json class/function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Tests for function output: get_json"""
        mockAttrs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**mockAttrs)) as mockGet:
            self.assertEqual(get_json(test_url), test_payload)
            mockGet.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unittest for memoize class/function"""
    def test_memoize(self) -> None:
        """Tests for function output: memoize"""
        class TestClass:
            """Unittest for memoize decorator class/function"""
            def a_method(self):
                """Method to return a fixed value"""
                return 42

            @memoize
            def a_property(self):
                """Method for memoize decorator to call a_method"""
                return self.a_method()
        with patch.object(TestClass, "a_method",
                          return_value=lambda: 42) as mockMethod:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mockMethod.assert_called_once()
