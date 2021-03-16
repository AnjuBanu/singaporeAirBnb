import unittest
import io
import sys
from test_process import TestProcess
from test_table import TestTable
from test_database import TestDatabase


def execute():
    suppress_text = io.StringIO()
    sys.stdout = suppress_text
    tc1 = unittest.TestLoader().loadTestsFromTestCase(TestProcess)
    tc2 = unittest.TestLoader().loadTestsFromTestCase(TestTable)
    tc3 = unittest.TestLoader().loadTestsFromTestCase(TestDatabase)
    sanity = unittest.TestSuite([tc1,tc2,tc3])
    unittest.TextTestRunner().run(sanity)


if __name__ == '__main__':
    execute()

