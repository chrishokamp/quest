

import pandas as pd

# load a file containining a single column, and add it to the passed dataframe

def append_column(df, new_column_filepath, new_column_name='bleu_backreference'):
    new_col = pd.io.parsers.read_table(new_column_filepath)
    df[new_column_name] = new_col.values
    return df 

# TODO: add a check to ensure that feature names aren't duplicated
def concatenate_feature_file(feature_file_name, df):
    new_features = pd.io.parsers.read_table(feature_file_name)
    return df.join(new_features)