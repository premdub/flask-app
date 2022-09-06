from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_priya():
    return "HELLO PRIYA!....I HOPE YOU ARE DOING WELLLLL....I HOPE YOU ENJOY AND ABLE TO GET THE CAREER YOU ENJOY AND SUCCESSFUL WITH IT.,,>>>"

@app.route('/careers')
def career():
    return "THIS IS CAREERS PAGE:  POPULAR CAREERS ARE IT MANAGER, PHYSICIAN, COMPUTER ENGINEER."

from flask import Flask
@app.route('/careers')
def careers():
    return "THIS IS CAREERS PAGE:  POPULAR CAREERS" 	 


		
							
@app.route('/HHA504')
def HHA504():
    return 'This is CLASS HHA504 PAGE!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
