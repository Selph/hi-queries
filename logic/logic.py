import logic.openinghours as openinghours
import logic.location as location
import logic.hama as hama
import logic.exams as exams
import logic.infohama as infohama
import logic.hamaid as hamaid

def filter_logic(question):
    if 'infohama' in question:
        return infohama.infohama()
    if 'hamadetail' in question:
        return hamaid.find_hama(question)
    if 'próf' in question or 'lokapróf' in question:
        return exams.find_exam(question)
    if 'háma' in question:
        return hama.find_hama(question)
    if 'hvenær' in question or 'opnunartími' in question or 'opnunar-tími' in question or 'opna' in question or 'opinn' in question:
        return openinghours.find_hours(question)
    if 'hvar' in question:
        return location.find_location(question)
    if len(question) > 0:
        return { 'nothing': True, 'head': 'Skildi ekki spurninguna... Prófaðu að nota spurnarfornöfn t.d. hvar/hvenær' }