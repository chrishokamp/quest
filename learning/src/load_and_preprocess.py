#!/usr/bin/env python
# encoding: utf-8

from __future__ import print_function
import numpy as np
import pandas as pd
import math
import logging

from pandas_utils import *

from experiment_logger import *

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
        
        # testing - join our new features with their baseline
#         features1 = pd.io.parsers.read_table('/home/chris/projects/quest-new/output/wmt2014/source.de.tok_to_target.en.tok.out')
#         features = features.join(features1)

        df = features

        scores = pd.io.parsers.read_table(scores_file_name)
        
        # Testing - remove the last feature
#         features = features.iloc[:,:-1]

        #df = features.join(scores)
        
        # WORKING - pseudo ref
        # TODO: move this to an optional preprocessing step
        # BING - EN ES
        # backref_score_path = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-es_training/pseudo_reference/en-es_backreference.bleu.out'
        # df = concatenate_feature_file(backref_score_path, df)
        
        # English-German
#         backref_score_path = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/en-de_backreference.bleu.out'
#         df = append_column(features, backref_score_path)

        # WORKING - decoder features
        # testing the moses decoder features for en-de backreferences
        # Lex 1-3 (don't improve performance)
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/LexicalReordering0.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/LexicalReordering1.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/LexicalReordering2.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)

        # Distortion (improves slightly)
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/Distortion.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)

        # Phrase-Translation-Probability 
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/Phrase-Translation-Probability.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)

        # Score 
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/Score.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)

        # LanguageModel0
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/LanguageModel0.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)

        # Lexical-Translation-Probability (THIS IMPROVES OVER THE BASELINE, but not together with the BLEU score :-/)
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/Lexical-Translation-Probability.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)

        # OSM0 (THIS IMPROVES OVER THE BASELINE, also together with Lexical-Translation-Probability)
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/OSM0.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)
        # testing just OSM features
#         df = pd.io.parsers.read_table(backref_decoder_lexical_scores)
        
        # PP 
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/PP.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)
        
        # WP (slight improvement over baseline)
        backref_decoder_lexical_scores = '/home/chris/projects/random_indexing/python/wmt2014/quality_estimation/data/perceived_PE_effort/task1-1_en-de_training/pseudo_reference/decoder_features/WP.tsv'
#         df = concatenate_feature_file(backref_decoder_lexical_scores, df)
        
        
#         print('dataframes bleu backref column: ')
#         print(df['bleu_backreference'])
        
        # so that scores will be the last column
        df = df.join(scores)

        # end pseudo ref
        
        # concat and drop zeros 
        df.fillna(0, inplace=True)
        
        # quick test - drop 10 features - in the first 10 features, some features DO make performance worse - which ones are these?
#         df = df.iloc[:, 10:]

        print("Before dropping zeros: DF shape:")
        print(df.shape)
        df, dropped_cols = drop_zeros(df)
        print("After dropping zeros: DF shape:")
        print(df.shape)
        
        # now do a random sample of the rows 
        train_data, test_data = \
            split_data(df, split_percentage)
        
        # LOGGING
        # set some interesting data on the logger
        logger.dropped_features = dropped_cols
        logger.features = df.columns.values.tolist()

        # map row indices to their (future) place in a numpy array
        test_rows = test_data.index.values.tolist()
        logger.test_data_row_map = {idx: x for idx,x in enumerate(test_rows)}
        # END LOGGING

        
        X_train = train_data.iloc[:,:-1]
        y_train = train_data.iloc[:,-1]
        
        X_test = test_data.iloc[:, :-1]
        y_test = test_data.iloc[:,-1]

        # in order to use cross validation, we just return the whole training data, and all of the scores
        all_training_data = df.ix[:,:-1]
        all_test_data = df.ix[:,-1]

        return X_train, y_train, X_test, y_test, all_training_data, all_test_data, logger
        
    except IOError as e:
        print("load_and_preprocess.prep_data_for_ml: Error loading files")
        raise
    
# TODO: fix error -- allows reselection of the same segments!
# TODO: get some hard-coded testing indices for each language pair
en_es_test_rows=[3459, 2698, 1083, 3174, 2012, 1292,  210, 2475, 3702,  389, 1625,
       3023, 2560, 1613, 2283, 3112, 3122,  690, 1110, 1412, 2828, 2914,
       2148,  210, 3730, 1977, 2928,  315, 1822, 2181,   42, 1274, 1346,
       1174, 2925,  619, 1807, 1055, 3254, 2014,  234, 1583, 1879, 2110,
       1782, 1252, 3216, 3202, 1056, 1408, 1591, 3676,  747, 3343, 3167,
        620,  210, 1482, 3358, 3192, 3715,  984, 2781, 2796, 3280, 2966,
       1659, 1316,  330,  158, 1852, 1125, 2729, 1969, 1113, 2585, 3088,
        963, 1467, 2004, 3781, 3711,  160, 1334, 2936,  195, 1324,  326,
       2125, 1938, 3803,  947, 1832, 2824, 3381,  281, 2345, 2464, 3352,
       1583, 3730, 3424,  793,  136, 1177, 1197,  716, 2073, 1325, 3754,
       1651, 1511,  139, 3500, 3580, 2860, 2787, 2404, 3222, 1845, 3240,
       3323, 3204,   56, 1822, 3074, 3569, 1422, 2066, 3702, 1433, 1856,
       1492,  737, 3008, 3131, 1995,  702, 1936, 2262, 1215, 2698,  663,
       1179, 3590, 1431,  411,  213, 2543, 3716, 1570, 1253,  936, 2136,
       2521, 1995,  943,  540, 2479, 3389, 1336, 1812, 2180, 2216, 1151,
       1072, 3497, 1773, 1407, 2584, 3115,   33, 2770, 2986, 2612,  122,
       3312,  426,  333, 1922,  814, 1927,  383,  935, 1641, 3272, 1647,
       1615,  117, 2799,   14, 1623, 2944, 2184,  467, 2054, 1851, 1064,
       2885,  233, 3067,  940, 3754, 2940,  391, 2048, 1393, 1608, 1330,
       3022, 2722, 3047, 2613,  881, 2272, 3281, 2564,  396,  154,  555,
       3193, 3807, 1850, 1224, 2510, 2068, 3153,  308, 2275,  633, 1260,
         92,  177, 1563, 1833, 3363, 2511, 2567, 1372, 1379, 1283, 1075,
       1487, 2762, 2263, 2109, 3283, 3668, 1121, 1487,  742,  798, 2639,
       2022, 1949,   70, 2910, 1279, 2811, 3017,  855, 2325,  268,  158,
       2681, 3275, 2978,  904, 3471, 1257,  188, 1515, 1197, 1089, 3334,
       1337, 2478, 2213, 2998, 1462,  510, 3426, 2690, 2032,  504, 1315,
       1054, 2825, 3741,   76, 2390,  971, 3348,  189,  466, 1374, 3228,
       3815, 2544, 2641, 2202, 3257,   92,  241, 1811, 1225,  774, 3092,
       1339,  815, 3785, 2916, 3542, 1415, 2075, 1381, 2185, 2544, 2137,
       3054, 3044, 3257,  930,  174, 1709, 3606,  758,  266, 2766, 2538,
        135,  774, 3453, 2616, 2259,  230, 2330, 3626,  445,  422,  700,
       3164, 1909, 2883,  977, 2596, 1809, 1236, 3448,  465, 1661,  362,
       3345, 1601, 3304,  112, 1828, 3058, 3811, 1707,  844,  499, 2715,
       3777, 3193, 1491, 2140, 3650,  787, 2392, 1701, 2163, 1207, 2532,
       1226,  313,  948, 2429, 1844, 1277,  399]

de_en_test_rows=[ 201,  267,  499,  224,  488,  458,  339,   60,  411,   17,  339,
        504,  172,  113,  819,  272,  974,  939,  913, 1040,  555,  765,
        651,  444,  773,  521,  607,  157,  151,  763,  402,    6,  841,
        737,    7,  268,  413,  287,  238,  391,  682,   35,  891, 1025,
        912,  239,  284,   80,  780,  595,  734,  722, 1028,  577,  453,
        379,   45,  208, 1047,  141, 1023, 1043,  773, 1031,  501,  206,
        518,   62,  214,  468,  338,  984,  568,  813,  888,   56,  689,
        589,  613,  919,  347,  975,  587,  364,  165,   78,   57,  122,
        519,  963,  988,  926,  426,  250,  268,  654,  354,  933,  538,
        868,  257,  135,  247,  276,  631]
en_de_test_rows=[  70,  483,  663, 1397,  912, 1358,  668,  160,  209,  973, 1153,
       1062,  653, 1398, 1362, 1033,  155,  447,  378, 1378,  167,  182,
        918, 1258,  531,  140,  426,  787,   16,  831,  421,  370,  498,
        429, 1096,  821,  683,  418,   89,  784,  406, 1112, 1304, 1366,
        796,  121,  919,   21,  519,  443, 1093,  927, 1172, 1342, 1174,
        922,  844,  764,  207,  985,  315,  621,  844, 1050,  295,  746,
        418,  648,  253,  949,  512,  702,  853,   57, 1221,  871,  184,
       1363, 1055,  399,  554, 1376,  151,  391,  853,  463,  920, 1390,
        499,   69, 1014,  292, 1329, 1377,  639,  189, 1363,  808,  643,
        612,  676,  908,  469,  506, 1251,  520,  499, 1388,  358,  347,
       1342,   70,  963,  553,  859, 1258,  974, 1365,  761, 1224, 1135,
       1394,  209,   52,  634,   13,  294,  897, 1291, 1209,  221,  488,
        641,  476,  482, 1290,  809,  607,   85,  396]

# ten_test_rows = [1,2,3,4,5,6,7,8,9]
task2_de_en_test_rows = [560, 773, 659, 490, 810, 731, 601, 518, 860, 697, 760, 862, 840,
       518, 608, 429, 551, 780,  52, 264, 416, 400, 287, 488, 343, 104,
       242, 708, 317, 811, 744, 190, 799, 279, 777, 382, 577, 759,  32,
       734, 773, 278, 426, 855, 420, 611, 774,  37, 764,  37, 282, 773,
       847,  19, 118, 271, 209, 211, 126, 214, 260, 882, 430, 805, 358,
       538, 502, 222, 255,  88, 697, 232, 509, 860, 316, 135, 528, 717,
       764,  77, 748, 421,  87, 109,  64, 180, 284, 607, 499]


def split_data(complete_frame, test_percent_split):
    print("split_data: complete_frame shape")
    print(complete_frame.shape)
    x_size = complete_frame.shape[0]
    test_data_size = math.floor(x_size / test_percent_split)

    print("len complete_frame index:")
    print(len(complete_frame.index.values))

    # TODO: don't allow duplicates in test_rows
    test_rows = np.random.choice(len(complete_frame.index), test_data_size)

    # testing with static row selection for each language pair
    #test_rows = de_en_test_rows 
#     test_rows = en_de_test_rows
    #test_rows = ten_test_rows 
#     test_rows = task2_de_en_test_rows
#     test_rows = en_es_test_rows
#    test_rows = mt_vs_human_test_rows 

#     print(complete_frame.index)
#     print(complete_frame.iloc[0,:])

#     print("TEST ROWS:")
#     print(json.dumps(test_rows))
    print("LEN TEST ROWS:")
    print(len(test_rows))

    test_data = complete_frame.iloc[test_rows,:]  
    print("split_data: test data shape")
    print(test_data.shape)

    train_data = complete_frame.drop(test_rows)
    print("split_data: train data shape")
    print(train_data.shape)

    return train_data, test_data

# add n^2 new features by computing the product of every feature pair (and removing duplicates)
def add_product_of_features(self): 
    pass
