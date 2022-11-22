import pandas as pd
import os
import numpy as np

def find_hama(question):
    df = dataprep()
    
    buildings = df["building"].to_numpy()
    id = 0
    if 'hama-oddi' in question:
        id = id = np.where(buildings == 'hamaoddi')[0][0]
    if 'eir-berg' in question:
        id = id = np.where(buildings == 'hamaeirberg')[0][0]
    if 'hama-salat-bar' in question:
        id = id = np.where(buildings == 'hamasalatbar')[0][0]
    for token in question:
        if len(np.where(buildings == token)[0]) > 0:
            id = np.where(buildings == token)[0][0]

    data = {
        'hama': False,
        'hamadetail': True, 
        'head': df.iloc[id]['name'],
        'weekdays': df.iloc[id]['opening week'],
        'sat': df.iloc[id]['opening sat'],
        'sun': df.iloc[id]['opening sun'],
        'address': df.iloc[id]['address']
        }
    
    return data


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/hama.csv')
    
    cols = ['building', 'name', 'opening week', 'opening sat', 'opening sun', 'address']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df