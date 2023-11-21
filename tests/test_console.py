#!/usr/bin/python3
"""A test module for the console"""
import unittest
from console import HBNBCommand
import MySQLdb
import os
import sqlalchemy
from io import StringIO
from unittest.mock import patch


class test_Console(unittest.TestCase):
    """Test for the console"""

    def test_documentation(self):
        """Test for the documentation"""
        self.assertIsNotNone(console.__doc__)
