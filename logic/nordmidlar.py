import util.dataprep as d
import numpy as np

def midlar(question):
    # Gives information about Nörd social media
    
    # Get dataframe
    cols = ['media','link']
    df = d.dataprep('nördmiðlar.csv', cols)

    # Get reference column
    media = df["media"].to_numpy()
        
    # Find correct answer row
    id = ''
    for token in question:
        if len(np.where(media == token)[0]) > 0:
            id = np.where(media == token)[0][0]
    
    # No media specified, return list of media
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
    
    # Information package
    data = {
        'nordmedia': True,
        'media': df.iloc[id]['media'],
        'link': df.iloc[id]['link']
        }
    
    return data