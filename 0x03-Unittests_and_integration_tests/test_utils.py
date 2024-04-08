#!/usr/bin/env python3
''' tests for util functions '''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    ''' class for unitesting '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        ''' tests the nested_map function for correct output '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        ''' tests that keyerror is raised for certain inputs '''
        with self.assertRaises(KeyError) as Error:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(Error.exception))


class TestGetJson(unittest.TestCase):
    ''' tests for get_json util '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, expected_response, mock_get):
        ''' tests that method called exactly once with url arg '''
        mock_get.return_value.json.return_value = expected_out

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, expected_out)


class TestMemoize(unittest.TestCase):
    ''' testing memoize '''

    def test_memoize(self):
        ''' test for correct result after calling a_property twice'''

        class TestClass:
            ''' helper class '''

            def a_method(self):
                ''' returns 42'''
                return 42

            @memoize
            def a_property(self):
                ''' returns a method'''
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
