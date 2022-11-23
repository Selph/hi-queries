import util.dataprep as d
import numpy as np

def nemendathjon(question):
    # Gives information about Nemendaþjónusta and SHÍ
    
    # Get dataframe
    cols = ['slug','name','phone','building','email','url']
    df = d.dataprep('nemendathjon.csv', cols)

    # Get reference column
    slug = df["slug"].to_numpy()

    # Matching lemmatizations with sheet
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
        
    # Find correct answer row
    id = ''
    for token in question:
        if len(np.where(slug == token)[0]) > 0:
            id = np.where(slug == token)[0][0]
    
    # Error
    if id == '':
        return {
            'nemendathjon2': True
        }
        
    # Information Package
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