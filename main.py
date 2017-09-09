from flask import Flask, render_template, request
from computation import formula

app = Flask(__name__)

@app.route('/result', methods = ['POST'])
def result():
	try:
		date_dd = int(request.form['date_dd'])
		date_mm = int(request.form['date_mm'])

		time_hours = int(request.form['time_hours'])
		time_minutes = int(request.form['time_minutes'])

		degrees_local = float(request.form['degrees_local'])
		minutes_local = float(request.form['minutes_local'])

		degrees_std = float(request.form['degrees_std'])
		minutes_std = float(request.form['minutes_std'])

		phi_degrees = float(request.form['phi_degrees'])
		phi_minutes = float(request.form['phi_minutes'])

		beta_angle = float(request.form['beta_angle'])

		gamma_angle = float(request.form['gamma_angle'])

		hemisphere = str(request.form['hemisphere'])

		result_list = formula.input_data_interface(date_dd, date_mm, time_hours, time_minutes, degrees_local, minutes_local, degrees_std, minutes_std, phi_degrees, phi_minutes, beta_angle, gamma_angle, hemisphere)

		return render_template('result.html', solar_time = str(result_list[0]), incidence_angle = str(result_list[1]))
	except:
		return render_template('error.html')

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)



'''march 59
april 90
may 120
june 151
july 181
august 212
sept 243
octo 273
nov 304
dec 334'''