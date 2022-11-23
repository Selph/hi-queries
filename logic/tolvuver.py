import util.dataprep as d
import numpy as np

def tolvuver():
    # Gives information about computer rooms in HÍ
    
    # Get dataframe
    cols = ['slug', 'name', 'address', 'building']
    df = d.dataprep('tolvuver.csv', cols)
    
    # Generate list of computer rooms
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

    # Information package
    data = {
        'tolvuver': True, 
        'head': 'Hér er listi yfir tölvuver',
        'tolvuverin': tolvuver
        }

    return data