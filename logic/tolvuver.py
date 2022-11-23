import pandas as pd
import os
import numpy as np

def tolvuver():
    df = dataprep()
    
    tolvuver = []
    i = 0
    for row in df.iterrows():
        tolvuver.append({
            'name': df.iloc[i]['name'],
            'address': df.iloc[i]['address'],
            'slug': df.iloc[i]['slug'],
            'building': df.iloc[i]['building']
            })
        i = i + 1

    data = {
        'tolvuver': True, 
        'head': 'Hér er listi yfir tölvuver',
        'tolvuverin': tolvuver
        }

    return data


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/tolvuver.csv')
    
    cols = ['slug', 'name', 'address', 'building']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df