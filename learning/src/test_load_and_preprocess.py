#!/usr/bin/env python
# encoding: utf-8

import unittest
import logging

from load_and_preprocess import *

#logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

class TestLoadAndPreprocess(unittest.TestCase):

    # setup -- create a new CKY instance
    def setUp(self):
        # load a test_tsv
        self.tsv = pd.io.parsers.read_table('test_tsv')


    # test that loading works
    def test_load_tsv(self):
        df = load_tsv('test_tsv')
        logging.debug('printing the dataframe...')
#         logging.debug(df)
        self.assertTrue(df.shape == self.tsv.shape, "a dataframe should load from tsv correctly")
        
    
    # test that zeroing works (we know that some cells are zero in the test dataset)
    def test_zero(self):
        # cells that are zero in the dataset: 1007, 1008, 1062, 1063, 1072, 1073
        zero_labels = ['1007', '1008', '1062', '1063', '1072', '1073']
        logging.debug(self.tsv.columns)
        original_cols = self.tsv.shape[1]
        self.assertTrue(len(self.tsv.loc[zero_labels].index) == 6, "the labels should exist in the original index")
        # remove the zeros
        no_zeros = drop_zeros(self.tsv)
        non_zero_cols = no_zeros.shape[1]
        logging.debug('num original cols is: %s' % str(original_cols))
        logging.debug('num cols after zeroing is: %s' % str(non_zero_cols))
        gte = original_cols - 6 >= non_zero_cols
        self.assertTrue(gte, "columns with only zeros should be dropped from the index")


    
    
if __name__ == '__main__':
    unittest.main()