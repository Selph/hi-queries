import util.dataprep as d
import numpy as np

def stjorn(question):
    # Gives information about Nörd management
    
    # Get dataframe
    cols = ['name','role','slug']
    df = d.dataprep('nördstjórn.csv', cols)

    # Get reference column
    slug = df["slug"].to_numpy()
        
    # Find correct answer row
    id = ''
    for token in question:
        if len(np.where(slug == token)[0]) > 0:
            id = np.where(slug == token)[0][0]
        
    # No role specified, return management list
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
    
    # Information package
    data = {
        'stjorn': True,
        'name': df.iloc[id]['name'],
        'role': df.iloc[id]['role']
        }
    
    return data