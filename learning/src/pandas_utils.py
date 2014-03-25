

import pandas as pd

# load a file containining a single column, and add it to the passed dataframe

def append_column(df, new_column_filepath):
    new_col = pd.io.parsers.read_table(new_column_filepath)
    df['bleu_backreference'] = new_col.values
    return df 