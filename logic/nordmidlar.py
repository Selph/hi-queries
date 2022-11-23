import pandas as pd
import os
import numpy as np

def midlar(question):
    df = dataprep()

    media = df["media"].to_numpy()
        
    id = ''
    
    for token in question:
        if len(np.where(media == token)[0]) > 0:
            id = np.where(media == token)[0][0]
        
    if id == '':
        data = []
        i = 0
        for row in df.iterrows():
            data.append({
                'media': df.iloc[i]['media'],
                'link': df.iloc[i]['link']
            })
            i = i + 1

        return {
            'nordmedialist': True,
            'medias': data
        }
        
    data = {
        'nordmedia': True,
        'media': df.iloc[id]['media'],
        'link': df.iloc[id]['link']
        }
    
    return data


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/nördmiðlar.csv')
    
    cols = ['media','link']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df