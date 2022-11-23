import util.dataprep as d
import numpy as np

def find_location(question):
    # Gives location information on HÍ buildings
    
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
        return 'Veit ekki hvar tiltæk bygging er eða bygging ekki á lista/rangt skrifuð'
    
    # Information package
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
