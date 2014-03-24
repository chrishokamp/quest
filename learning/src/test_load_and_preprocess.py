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
        self.tsv = pd.io.parsers.read_table('test_data_tsv')
        self.features_filename = 'test_data_tsv'
        self.scores_filename = 'test_scores_tsv'

    # test that loading works
    def test_load_tsv(self):
        df = load_tsv(self.features_filename)
        logging.debug('printing the dataframe...')
#         logging.debug(df)
        self.assertTrue(df.shape == self.tsv.shape, "a dataframe should load from tsv correctly")
        
    
    # test that zeroing works (we know that some cells are zero in the test dataset)
    def test_zero(self):
        # some of the cells that are zero in the dataset: 1007, 1008, 1062, 1063, 1072, 1073
        zero_labels = ['1007', '1008', '1062', '1063', '1072', '1073']
        logging.debug(self.tsv.columns)
        original_cols = self.tsv.shape[1]
        self.assertTrue(len(self.tsv.loc[zero_labels].index) == 6, "the labels should exist in the original index")
        # remove the zeros
        no_zeros, drop_cols = drop_zeros(self.tsv)
        non_zero_cols = no_zeros.shape[1]
        logging.debug('num original cols is: %s' % str(original_cols))
        logging.debug('num cols after zeroing is: %s' % str(non_zero_cols))
        gte = original_cols - 6 >= non_zero_cols
        self.assertTrue(gte, "columns with only zeros should be dropped from the index")
        
    
    def test_prep_data_for_ml(self):
        X_train_frame, y_train_frame, X_test_frame, y_test_frame, logger = \
            prep_data_for_ml(self.features_filename, self.scores_filename)
            
        # check mapping from pandas row indices to np.ndarray row values
        print("X_train_frame rows: ")
        print(X_train_frame.index.values)
        print("X_test_frame rows: ")
        print(X_test_frame.index.values)
        
        self.assertTrue(X_train_frame.shape[1] == X_test_frame.shape[1], "the train and test indices should have the same shape")
        self.assertTrue(X_train_frame.shape[0] == len(y_train_frame), "the scores should have the same number of rows as the features")
        self.assertTrue(X_test_frame.shape[0] == len(y_test_frame), "the scores should have the same number of rows as the features")
        
    def test_logging(self):
        pass

    
if __name__ == '__main__':
    unittest.main()