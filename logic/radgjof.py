import pandas as pd
import os
import numpy as np

def radgjof():
    df = dataprep()

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


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/radgjof.csv')
    
    cols = ['slug','name','phone','opening','email','address','url']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df