import util.dataprep as d
import numpy as np

def radgjof():
    # Gives information about HÍ support desks
    
    # Get dataframe
    cols = ['slug','name','phone','opening','email','address','url']
    df = d.dataprep('radgjof.csv', cols)

    # Generic information package
    data = {
        'radgjof': True,
        'head': df.iloc[1]['name'],
        'phone': df.iloc[1]['phone'],
        'opening': df.iloc[1]['opening'],
        'email': df.iloc[1]['email'],
        'address': df.iloc[1]['address'],
        'url': df.iloc[1]['url']
        }
    
    return data