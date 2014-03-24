#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import numpy as np
import pandas as pd
import math
import logging

from experiment_logger import *

# TODO: make a dataobject which can keep the feature indices in order?

def load_tsv(filename):
    try:
        return pd.io.parsers.read_table(filename)
    except IOError as e:
        print("Error loading file: " + filename)
        raise
    
# drop features which are always zero (these can mess up the scikit learn scaling)
def drop_zeros(df):
    # create a Series with the sum of every column as the values
    summed_cols = df.sum()
    no_zeros = df.loc[:, [col for col in summed_cols.index if summed_cols[col] != 0.0]]
    drop_cols = [col for col in summed_cols.index if summed_cols[col] == 0.0]

    return no_zeros, drop_cols

# combine load_tsv and drop_zeros into a pipeline which returns ndarrays
def preprocess(tsv_filename):
    df = load_tsv(tsv_filename)
    no_zeros = drop_zeros(df)

    return no_zeros

def load_files(file_list):
    return [preprocess(file) for file in file_list]

# note: both files are expected to have the column labels as the first row
def prep_data_for_ml(features_file_name, scores_file_name, logger=True):
    
    logger_filename = 'ml_experiments.log'
    logger = ExperimentLogger(logger_filename)
    
# TODO: pass split_percentage as argument
    split_percentage = 10
    
    try:
        features = pd.io.parsers.read_table(features_file_name)
        scores = pd.io.parsers.read_table(scores_file_name)
        df = features.join(scores)
        
        # concat and drop zeros 
        df.fillna(0, inplace=True)

        df, dropped_cols = drop_zeros(df)
        
        
        # now do a random sample of the rows 
        train_data, test_data = \
            split_data(df, split_percentage)
        
        # set some interesting data on the logger
        logger.dropped_features = dropped_cols
        logger.features = df.columns.values
        # map row indices to their (future) place in a numpy array
        test_rows = test_data.index.values
        logger.test_data_row_map = {idx: x for idx,x in enumerate(test_rows)}
        
        X_train = train_data.iloc[:,:-1]
        y_train = train_data.iloc[:,-1]
        
        X_test = test_data.iloc[:, :-1]
        y_test = test_data.iloc[:,-1]

        return X_train, y_train, X_test, y_test, logger
        
    except IOError as e:
        print("load_and_preprocess.prep_data_for_ml: Error loading files")
        raise
        
    
def split_data(complete_frame, test_percent_split):
    x_size = complete_frame.shape[0]
    test_data_size = math.floor(x_size / test_percent_split)

    test_rows = np.random.choice(complete_frame.index.values, test_data_size)

    test_data = complete_frame.ix[test_rows]  
    train_data = complete_frame.drop(test_rows)

    return train_data, test_data
