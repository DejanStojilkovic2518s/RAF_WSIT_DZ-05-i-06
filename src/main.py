from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('raspored_casova.html')

@app.route('/raspored')
def raspored():
	f = open("raspored.csv", "r")
	redovi = f.readlines()
	ime_predavaca = [red.split(',')[2] for red in redovi]
	jedinstvena_imena = []
	for ime in ime_predavaca:
		if ime not in jedinstvena_imena:
			jedinstvena_imena.append(ime)

	ucionice = [red.split(',')[6] for red in redovi]
	jedna_ucionica = []
	for ucionica in ucionice:
		if ucionica not in jedna_ucionica:
			jedna_ucionica.append(ucionica)

	return render_template("raspored_casova.html", redovi = redovi, jedinstvena_imena = jedinstvena_imena, jedna_ucionica = jedna_ucionica)


if __name__ == '__main__':
	app.run()