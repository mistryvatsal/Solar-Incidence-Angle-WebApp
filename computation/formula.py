from math import sin, cos, acos, asin, radians, degrees

# A function to take the input data and call the computing functions respectively.
def input_data_interface(date_dd, date_mm, time_hours, time_minutes, degrees_local, minutes_local, degrees_std, minutes_std, phi_degrees, phi_minutes, beta_angle, gamma_angle, hemisphere):
	n = compute_days(date_dd, date_mm)
	std_time_in_mins = compute_time(time_hours, time_minutes)
	L_loc = compute_longi(degrees_local, minutes_local)
	L_std = compute_longi(degrees_std, minutes_std)
	phi = compute_longi(phi_degrees, phi_minutes)
	
	solar_time = compute_solar_time(n, std_time_in_mins, L_std, L_loc, hemisphere)
	solar_time_minutes = solar_time % 60
	solar_time = solar_time / 60
	final_solar_time = str(int(solar_time)) + ' hours, ' + str(int(solar_time_minutes)) + 'minutes.'
	
	incidence_angle = round(compute_incidence_angle(n, solar_time, phi, beta_angle, gamma_angle), 2)
	return [final_solar_time, incidence_angle]

#A function to compute longitude in decimal.
def compute_longi(degrees, minutes):
	return degrees + minutes / 60

#A function to compute number of days based upon days.
def compute_days(date_dd, date_mm):
	if date_mm == 1:
		days = date_dd

	if date_mm == 2:
		days = 31 + date_dd

	if date_mm == 3:
		days = 59 + date_dd

	if date_mm == 4:
		days = 90 + date_dd

	if date_mm == 5:
		days = 120 + date_dd

	if date_mm == 6:
		days = 151 + date_dd

	if date_mm == 7:
		days = 181 + date_dd

	if date_mm == 8:
		days = 212 + date_dd

	if date_mm == 9:
		days = 243 + date_dd

	if date_mm == 10:
		days = 273 + date_dd

	if date_mm == 11:
		days = 304 + date_dd

	if date_mm == 12:
		days = 334 + date_dd
	
	return days

#A function to compute time.
def compute_time(time_hours, time_minutes):
	std_time = (time_hours * 60) + time_minutes
	return std_time


#A function to compute solar time.
def compute_solar_time(n, std_time_in_mins, L_std, L_loc, hemisphere):
	delta = 23.45 * sin(radians(360*(284+n)/365))
	B = 360*(n-81)/364
	E = 9.87 * sin(radians(2*B)) - 7.53 * cos(radians(B)) - 1.5 * sin(radians(B))
	if hemisphere == 'eastern_hemisphere':
		solar_time = std_time_in_mins - 4 * (L_std - L_loc) + E
	if hemisphere == 'western_hemisphere':
		solar_time = std_time_in_mins + 4 * (L_std - L_loc) + E
	
	return solar_time


#A function to compute Incidence Angle.
def compute_incidence_angle(n, solar_time, phi, beta_angle, gamma_angle):
	delta = 23.45 * sin(radians(360*(284+n)/365))
	omega = (12.00 - solar_time) * 15
	cos_incidence_angle = (cos(radians(phi)) * cos(radians(beta_angle)) + sin(radians(phi)) * sin(radians(beta_angle)) * cos(radians(gamma_angle))) * cos(radians(omega))*cos(radians(delta)) + cos(radians(delta)) * sin(radians(beta_angle)) * sin(radians(omega)) * sin(radians(gamma_angle)) + sin(radians(delta)) * (sin(radians(phi)) * cos(radians(beta_angle)) - cos(radians(phi)) * sin(radians(beta_angle)) * cos(radians(gamma_angle)))
	incidence_angle = degrees(acos(cos_incidence_angle))
	return incidence_angle
	