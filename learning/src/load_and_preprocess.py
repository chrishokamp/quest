#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import numpy as np
import pandas as pd
import logging

# TODO: make a dataobject which can keep the feature indices in order?

def load_tsv(filename):
    try:
        return pd.io.parsers.read_table(filename)
    except IOError as e:
        print("Error loading file: " + filename)
        raise
    
# drop features which are always zero (these can mess up the scikit learn scaling)
def drop_zeros(df):
    summed_cols = df.sum()
    no_zeros = df.loc[:, [col for col in summed_cols.index if summed_cols[col] != 0.0]]
    return no_zeros

# combine load_tsv and drop_zeros into a pipeline which returns ndarrays
def preprocess(tsv_filename):
    df = load_tsv(tsv_filename)
    no_zeros = drop_zeros(df)

    return no_zeros.values

def load_files(file_list):
    return [preprocess(file) for file in file_list]

# TODO: implement
def drop_nan(self):
    pass