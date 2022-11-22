import pandas as pd
import os
import numpy as np

def find_exam(question):
    df = dataprep()
    
    course = df["course"].str.lower().to_numpy()
    
    id = ''
    for token in question:
        if len(np.where(course == token)[0]) > 0:
            id = np.where(course == token)[0][0]
    
    if id == '':
        return 'Veit ekki hvenær tiltækt próf er eða áfangi ekki á lista/rangt skrifaður'
    data = {'exam': True,
            'head': 'Prófið í ' + df.iloc[id]['name'] + ' er á eftirfarandi tíma:',
            'date': df.iloc[id]['date'] }
    return data


def dataprep():
    basedir = os.path.abspath(os.path.dirname(__file__))
    data_file = os.path.join(basedir, '../static/sheets/exams.csv')
    
    cols = ['course', 'name', 'type', 'amount', 'date']
    df = pd.read_csv(data_file, names=cols, header=0)
    
    return df