from src.process.listingUtil import ListingUtil
import os.path
import tempfile
import unittest
from unittest.mock import patch


class TestProcess(unittest.TestCase):
    tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")
    def setUp(self):
        with open(self.tmpfilepath,'w') as f:
            f.write("Now the file has more content!")

    def test_cleanFiles(self):
        ListingUtil.cleanFiles(self.tmpfilepath)
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

    @patch('builtins.input', side_effect=['1', 'Select * from HOST'])
    def test_getJobInputs1(self, input):
        self.assertEqual(ListingUtil().getJobInputs(), True)


    @patch('builtins.input', side_effect=['2', 'Insert into host("ID","NAME") values (1,"newEntry")'])
    def test_getJobInputs2(self, input):
        self.assertEqual(ListingUtil().getJobInputs(), True)


    @patch('builtins.input', side_effect=['4', 'Delete from host where id = 1'])
    def test_getJobInputs3(self, input):
        self.assertEqual(ListingUtil().getJobInputs(), True)

    @patch('builtins.input', side_effect=['5'])
    def test_getJobInputs4(self, input):
        with self.assertRaises(SystemExit) as cm:
            ListingUtil().getJobInputs()
        self.assertEqual(cm.exception.code, 1)

    @patch('builtins.input', side_effect=['10'])
    def test_getJobInputs5(self, input):
        self.assertEqual(ListingUtil().getJobInputs(), False)


if __name__  == "__main__":
    unittest.main()