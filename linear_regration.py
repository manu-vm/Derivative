xi_yi = ((1,2),(2,4))

theta_0 = 0
theta_1 = 0
delta = 0.1
m = len(xi_yi)
loop = 200
for i in range(loop):
	#step 1 for find y hat
	y_hats = []
	for point in xi_yi:
		y_hat = theta_0+theta_1*point[0]
		y_hats.append(y_hat)

	#step 2 for find j
	j=0
	j_list = [0]
	for point,yHat in zip(xi_yi,y_hats):
		j = j +(point[1]-yHat)**2
	j = j/(2*m)
	j_list.append(j)
	if j>j_list[-1] and i>0:
		delta = delta-0.01
		print("Hello")
		continue
    
	# step 3 for find partial derivative of theta 0
	slope_theta_0 = 0
	for point,yHat in zip(xi_yi,y_hats):
		slope_theta_0 = slope_theta_0 +((point[1]-yHat))*-1
	slope_theta_0 = slope_theta_0/m

	# step 3 for find partial derivative of theta 0
	slope_theta_1 = 0
	for point,yHat in zip(xi_yi,y_hats):
		slope_theta_1 = slope_theta_1 +((point[1]-yHat))*point[0]*-1
	slope_theta_1 = slope_theta_1/m

	#step 4 for find new theta and equation of line
	theta_0 = theta_0-(delta*slope_theta_0)
	theta_1 = theta_1-(delta*slope_theta_1)

	slope = round(theta_0,5)
	constant = round(theta_1,5)
	sign = "+"
	if constant<0:
		constant = -constant
		sign="-"

	line_equation = f"y = {slope}x {sign} {constant}"
	print(line_equation)