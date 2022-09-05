from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_priya():
    return 'HELLO PRIYA!'

@app.route('/careers')
def careers():
    return 'THIS IS A CAREERS PAGE!'

@app.route('/HHA504')
def HHA504():
    return 'This is CLASS HHA504 PAGE!'

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)
