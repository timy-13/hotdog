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
        input_text = sentence.lineInput(text)
        processed_text_list = ['\n']
        for line in input_text:
            processed_text_list.append(sentence.questionGen(line))
        processed_text1 = '\n'.join(processed_text_list)
    return render_template('main.html', taname = input_text, processed_text = processed_text1)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)