#!/usr/bin/env python
# encoding: utf-8

import unittest
import logging

# from load_and_preprocess import *
from pandas_utils import *

#logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

class TestPandasUtils(unittest.TestCase):

    # setup -- create a new CKY instance
    def setUp(self):
        # load a test_tsv
        self.tsv = pd.io.parsers.read_table('test_data_tsv')
        

    # test that loading works
    def test_append_column(self):
        new_col_path = 'backreference_sample_col'
        new_df = append_column(self.tsv, new_col_path)
        print(new_df['bleu_backreference'])
        
#         self.assertTrue(df.shape == self.tsv.shape, "a dataframe should load from tsv correctly")
        
if __name__ == '__main__':
    unittest.main()