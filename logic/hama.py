import pandas as pd
import os
import numpy as np

def find_hama(question):
    df = dataprep()
    
    hamas = []
    i = 0
    for row in df.iterrows():
        hamas.append({
            'name': df.iloc[i]['name'],
            'building': df.iloc[i]['building']
            })
        i = i + 1

    data = {
        'hama': True, 
        'head': 'Opnunartímar og staðsetningar Hámu:',
        'hamas': hamas
        }
    return data


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/hama.csv')
    
    cols = ['building', 'name', 'opening week', 'opening sat', 'opening sun', 'address']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df