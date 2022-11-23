import util.dataprep as d

def find_hama(question):
    # Gives a list of Hámas
    
    # Get dataframe
    cols = ['building', 'name', 'opening week', 'opening sat', 'opening sun', 'address']
    df = d.dataprep('hama.csv', cols)
    
    # Generate list
    hamas = []
    i = 0
    for row in df.iterrows():
        hamas.append({
            'name': df.iloc[i]['name'],
            'building': df.iloc[i]['building']
            })
        i = i + 1

    # Information package
    data = {
        'hama': True, 
        'head': 'Opnunartímar og staðsetningar Hámu:',
        'hamas': hamas
        }
    
    return data