import numpy as np
import util.dataprep as d

def find_exam(question):
    # Matches an exam with sheet and returns the name and date of the test
    
    # Get dataframe
    cols = ['course', 'name', 'type', 'amount', 'date']
    df = d.dataprep('exams.csv', cols)
    
    # Get reference column
    course = df["course"].str.lower().to_numpy()
    
    # Find correct answer row
    id = ''
    for token in question:
        if len(np.where(course == token)[0]) > 0:
            id = np.where(course == token)[0][0]
    
    # Error
    if id == '':
        return 'Veit ekki hvenær tiltækt próf er eða áfangi ekki á lista/rangt skrifaður'
    
    # Information package
    data = {'exam': True,
            'head': 'Prófið í ' + df.iloc[id]['name'] + ' er á eftirfarandi tíma:',
            'date': df.iloc[id]['date'] }
    return data