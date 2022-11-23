import pandas as pd
import os
import numpy as np

def nemendathjon(question):
    df = dataprep()

    slug = df["slug"].to_numpy()

    if 'hugvísindasvið' in question or 'hugur' in question:
        question.append("hugs")
    if 'félagsvísindasvið' in question:
        question.append("fvs")
    if 'menntavísindasvið' in question:
        question.append("mvs")
    if 'heilbrigðisvísindasvið' in question:
        question.append("hvs")
    if 'stúdentaráð' in question:
        question.append("shi")
        
    id = ''
    
    for token in question:
        if len(np.where(slug == token)[0]) > 0:
            id = np.where(slug == token)[0][0]
        
    if id == '':
        return {
            'nemendathjon2': True
        }
        
    data = {
        'nemendathjon': True,
        'head': df.iloc[id]['name'],
        'phone': df.iloc[id]['phone'],
        'building': df.iloc[id]['building'],
        'email': df.iloc[id]['email'],
        'url': df.iloc[id]['url'],
        'slug': df.iloc[id]['slug']
        }
    
    return data


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/nemendathjon.csv')
    
    cols = ['slug','name','phone','building','email','url']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df