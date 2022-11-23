import util.dataprep as d
import numpy as np

def find_hama(question):
    # Gives information about specific Háma
    
    # Get dataframe
    cols = ['building', 'name', 'opening week', 'opening sat', 'opening sun', 'address']
    df = d.dataprep('hama.csv', cols)
    
    # Get reference column
    buildings = df["building"].to_numpy()
    
    # Have to specify certain lemmatizations
    if 'hama-oddi' in question:
        id = id = np.where(buildings == 'hamaoddi')[0][0]
    if 'eir-berg' in question:
        id = id = np.where(buildings == 'hamaeirberg')[0][0]
    if 'hama-salat-bar' in question:
        id = id = np.where(buildings == 'hamasalatbar')[0][0]
        
    # Find correct answer row
    id = 0
    for token in question:
        if len(np.where(buildings == token)[0]) > 0:
            id = np.where(buildings == token)[0][0]

    # Information package
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