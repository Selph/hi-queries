import util.dataprep as d
import numpy as np

from flask import request

def find_hours(question):
    # Gives opening hours of HÍ buildings
    
    # Get dataframe
    cols = ['building', 'name', 'opening week', 'opening sat', 'opening sun', 'address', 'url']
    df = d.dataprep('locations.csv', cols)
    
    # Get reference column
    buildings = df["building"].to_numpy()
    
    # Have to specify certain lemmatizations
    if 'vr' in question:
        if 'iii' in question or '3' in question:
            question.append("vr3")
        if 'ii' in question or '2' in question:
            question.append("vr2")
        if 'I' in question or '1' in question:
            question.append("vr1")
    
    # Find correct answer row
    id = ''
    for token in question:
        if len(np.where(buildings == token)[0]) > 0:
            id = np.where(buildings == token)[0][0]
            
    # Error
    if id == '':
        return 'Veit ekki hvenær tiltæk bygging opnar eða bygging ekki á lista/rangt skrifuð'
    
    # Information package
    data = {'hours': True,
            'name': df.iloc[id]['building'],
            'head': 'Byggingin ' + df.iloc[id]['name'] + ' er opin á eftirfarandi tímum:',
            'weekdays': 'Virkir dagar: ' + df.iloc[id]['opening week'],
            'sat': 'Laugardagar: ' + df.iloc[id]['opening sat'],
            'sun': 'Sunnudagar: ' + df.iloc[id]['opening sun'],
            'address': df.iloc[id]['address'],
            'url': df.iloc[id]['url']
            }
    
    return data