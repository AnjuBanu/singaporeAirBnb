
from src.database.database_operations import Database
from src.database.crud_operations import Crud
import sqlite3
from unittest.mock import MagicMock,Mock
import unittest
import io
import sys

class TestDatabase(unittest.TestCase):

    def setUp(self):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text


    def test_sqlite3_connect_success(self):
        sqlite3.connect = MagicMock(return_value='connection succeeded')
        conn = Database(None).connect("test_database")
        sqlite3.connect.assert_called_with('test_database')
        self.assertEqual(conn, 'connection succeeded')

    def test_sqlite3_connect_failure(self):
        sqlite3.connect = MagicMock(return_value='connection failure')
        conn = Database(None).connect("test_database")
        sqlite3.connect.assert_called_with('test_database')
        self.assertEqual(conn, 'connection failure')


if __name__ == '__main__':
    unittest.main()