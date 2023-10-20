import pandas as pd 
from typing import List


"""
Função para transformar uma lista de dataframes em um únocp dataframe
"""

def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)