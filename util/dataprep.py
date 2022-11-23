import pandas as pd
import os

def dataprep(data, cols):
    # Loads a dataframe with pandas
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    data_file = os.path.join(basedir, '../static/sheets/' + data)
    
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df