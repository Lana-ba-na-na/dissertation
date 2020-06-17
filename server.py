from flask import Flask, request, render_template
import pro

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
	results = pro.prof_area()
	return render_template('index.html', results=results)

@app.route('/prof_standard', methods=['POST','GET'])
def prof_standard():
	_prof_area = "Связь, информационные и коммуникационные технологии"
	_prof_name = "Программист"
	_education = request.form['education']

	if _prof_area and _prof_name:

		results = pro.main(_prof_area, _prof_name, _education)

	return render_template('prof_standard.html', results=results)

if __name__ == "__main__":
    app.run()