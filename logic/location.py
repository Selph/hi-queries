import pandas as pd
import os
import numpy as np

def find_location(question):
    df = dataprep()
    
    buildings = df["building"].to_numpy()
    id = ''
    if 'vr' in question:
        if 'iii' in question or '3' in question:
            question.append("vr3")
        if 'ii' in question or '2' in question:
            question.append("vr2")
        if 'I' in question or '1' in question:
            question.append("vr1")
    for token in question:
        if len(np.where(buildings == token)[0]) > 0:
            id = np.where(buildings == token)[0][0]
    if id == '':
        return 'Veit ekki hvar tiltæk bygging er eða bygging ekki á lista/rangt skrifuð'
    data = {'location': True,
            'name': df.iloc[id]['building'],
            'head': 'Byggingin ' + df.iloc[id]['name'] + ' er staðsett við:',
            'address': df.iloc[id]['address'],
            'url': df.iloc[id]['url'],
            'weekdays': 'Virkir dagar: ' + df.iloc[id]['opening week'],
            'sat': 'Laugardagar: ' + df.iloc[id]['opening sat'],
            'sun': 'Sunnudagar: ' + df.iloc[id]['opening sun']
            }
    return data


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/locations.csv')
    
    cols = ['building', 'name', 'opening week', 'opening sat', 'opening sun', 'address', 'url']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df