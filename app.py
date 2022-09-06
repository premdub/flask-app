from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_priya():
    return 'HELLO PRIYA!....I HOPE YOU ARE DOING WELLLLL....


@app.route('/careers')
def careers():
	POPULAR CAREERS = {
		"1" : 	"Dentist",	
		"2"	:	"Registered Nurse",	
		"3"	:	"Pharmacist",	
		"4"	:	"Computer Systems Analyst",	
		"5"	:	"Physician",	
		"6"	:	"Database Administrator",
		"7"	:	"Software Developer",	
		"8"	:	"Physical Therapist",	
		"9"	:	"Web Developer",	
		"10":	"Dental Hygienist",	
		"11":	"Occupational Therapist",
		"12":	"Veterinarian",	
		"13":	"Computer Programmer",	
		"14":	"School Psychologist",	
	}
    return POPULAR CAREERS

@app.route('/HHA504')
def HHA504():
    return 'This is CLASS HHA504 PAGE!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
