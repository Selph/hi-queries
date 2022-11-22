from flask import Flask, render_template, request, escape
import os

import util.tokenizer
 
app = Flask(__name__)

@app.route("/")
def index():
    question = str(escape(request.args.get("question", "")))
    if question:
        answer = answer_from(question)
    else:
        answer = ""
    return (
        render_template('page.html', answer=answer)
    )

def answer_from(question):
    """Svarar spurningu um HÍ"""
    try:
        return answer_algorithm(str(question))
    except ValueError:
        return "Ég veit ekki svarið... reyndu aftur!"
    
def answer_algorithm(question):
    tokens = util.tokenizer.question_processing2(question)
    return tokens

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=8080, debug=True)
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    
