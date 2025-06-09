from flask import Flask, render_template, jsonify
from AppOpener import open
from AppOpener import close
app = Flask(__name__)


def my_python_function():
    return open("whatsapp")


@app.route('/run-function', methods=['POST'])
def run_function():
    result = my_python_function()
    return jsonify({result})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

def my_python_function2():
    return close("whatsapp")


@app.route('/run-function', methods=['POST'])
def run_function():
    result = my_python_function2()
    return jsonify({result})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
