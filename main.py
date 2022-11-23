from flask import Flask, render_template, request, escape
import os
import pandas as pd

import util.tokenizer as tokenizer
import logic.logic as logic
 
app = Flask(__name__)

@app.route("/")
def index():
    # Takes a question from user
    question = str(escape(request.args.get("question", "")))
    
    # Returns the answer if there is a question
    if question:
        lemmas, answer = answer_from(question)
    else:
        lemmas, answer = "", ""
        
    # Renders html
    return (
        render_template('page.html', lemmas=lemmas, answer=answer)
    )

def answer_from(question):
    # Answers a question about HÍ
    try:
        return answer_algorithm(str(question))
    except ValueError:
        return "Ég veit ekki svarið... reyndu aftur!"
    
def answer_algorithm(question):
    # Prepares the input for the filter logic
    lemmas = tokenizer.question_processing2(question)
    
    # Finds a relevant answer
    answer = logic.filter_logic(lemmas)
    
    return lemmas, answer

if __name__ == "__main__":
    # For both the railway server and development server
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    
