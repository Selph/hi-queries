import pandas as pd
import os
import numpy as np

def stjorn(question):
    df = dataprep()

    slug = df["slug"].to_numpy()
        
    id = ''
    
    for token in question:
        if len(np.where(slug == token)[0]) > 0:
            id = np.where(slug == token)[0][0]
        
    if id == '':
        data = []
        i = 0
        for row in df.iterrows():
            data.append({
                'name': df.iloc[i]['name'],
                'role': df.iloc[i]['role']
            })
            i = i + 1

        return {
            'stjorn2': True,
            'team': data
        }
        
    data = {
        'stjorn': True,
        'name': df.iloc[id]['name'],
        'role': df.iloc[id]['role']
        }
    
    return data


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/nördstjórn.csv')
    
    cols = ['name','role','slug']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df