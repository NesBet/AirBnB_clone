#!/usr/bin/python3
"""
Unittest for console.py
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommandMethods(unittest.TestCase):
    """Tests instances for the  console."""

    def setUp(self):
        """Tests if class exists"""
        self.console = HBNBCommand()
        self.patcher = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.patcher.start()

    def tearDown(self):
        """Tests for a tear down."""
        self.patcher.stop()

    def test_create(self):
        """Test for creation"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(output.isalnum())  # Ensure it's a valid ID

    def test_show(self):
        """Test for existence."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            self.console.onecmd(f"show BaseModel {created_output}")
            show_output = mock_stdout.getvalue().strip()
            self.assertIn(created_output, show_output)

    def test_update(self):
        """Test for update case."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd("create BaseModel")
            created_output = mock_stdout.getvalue().strip()
            self.console.onecmd(f"update BaseModel {created_output} name 'NewName'")
            self.console.onecmd(f"show BaseModel {created_output}")
            show_output = mock_stdout.getvalue().strip()
            self.assertIn("NewName", show_output)

if __name__ == '__main__':
    unittest.main()
