from flask import Flask
from flask import Flask, request, url_for, render_template, redirect
import sentence

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        text = request.form.get('taname')
        input_text = text.upper()
        processed_text1 = sentence.questionGen(input_text)
    return render_template('main.html', taname = input_text, processed_text = processed_text1)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)