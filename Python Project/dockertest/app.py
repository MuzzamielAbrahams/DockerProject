from flask import Flask, request, render_template
from pythonmain import *
from ast import literal_eval

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    array_input = request.form['text']
    array_input = literal_eval(array_input)
    sorted_array = bubbleSort(array_input)
    return "["+",".join(map(str,sorted_array))+"]"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
