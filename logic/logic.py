import logic.openinghours as openinghours
import logic.location as location
import logic.hama as hama
import logic.exams as exams
import logic.infohama as infohama
import logic.hamaid as hamaid
import logic.tolvuver as tolvuver
import logic.radgjof as radgjof
import logic.nemendathjon as nemendathjon
import logic.nordstjorn as nordstjorn
import logic.nordmidlar as nordmidlar

def filter_logic(question):
    if 'nörd' in question:
        if 'forseti' in question or 'ritari' in question or 'gjaldkeri' in question or 'skemmtana-stjóra' in question or 'samfélagsmiðill' in question or 'hagsmuna-fulltrúi' in question or 'nýnema-fulltrúi' in question or 'stjórn' in question:
            return nordstjorn.stjorn(question)
        if 'discord' in question or 'facebook' in question or 'instagram' in question or 'insta' in question or 'fésbók' in question or 'miðill' in question:
            return nordmidlar.midlar(question)
    if 'nemenda-þjónusta' in question or 'von' in question or 'hugur' in question or 'hugvísindasvið' in question or 'fvs' in question or 'félagsvísindasvið' in question or 'menntavísindasvið' in question or 'mvs' in question or 'heilbrigðisvísindasvið' in question or 'hvs' in question or 'nemendaþjónusta' in question or 'stúdentaráð' in question or 'shí' in question:
        return nemendathjon.nemendathjon(question)
    if 'tölvuver' in question:
        return tolvuver.tolvuver()
    if 'námsráðgjöf' in question or 'starfsráðgjöf' in question or 'ráðgjöf' in question or 'sálfræðingur' in question:
        return radgjof.radgjof()
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