from flask import Flask, render_template, request, escape
import os
import pandas as pd

import util.tokenizer as tokenizer
import logic.logic as logic
 
app = Flask(__name__)

@app.route("/")
def index():
    question = str(escape(request.args.get("question", "")))
    if question:
        lemmas, answer = answer_from(question)
    else:
        lemmas, answer = "", ""
    return (
        render_template('page.html', lemmas=lemmas, answer=answer)
    )

def answer_from(question):
    """Svarar spurningu um HÍ"""
    try:
        return answer_algorithm(str(question))
    except ValueError:
        return "Ég veit ekki svarið... reyndu aftur!"
    
def answer_algorithm(question):
    lemmas = tokenizer.question_processing2(question)
    answer = logic.filter_logic(lemmas)
    return lemmas, answer

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    
