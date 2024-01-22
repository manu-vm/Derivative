delta   = 0.5
loop    = 100000
def Feature_Scaling(lis):
	R                = len(lis)
	mean_lis         = sum(lis)/R
	max_lis          = max(lis)
	min_lis          = min(lis)
	max_minus_min    = max_lis- min_lis
	lis              = [((i-mean_lis)/max_minus_min) for i in lis]
	return lis
def Price_of_a_house(pli_area,no_bedroom,no_floor,Dis_school):
	return theta_0+(theta_1*pli_area)+(theta_2*no_bedroom)+(theta_3*no_floor)+(theta_4*Dis_school)

	

plinth_area               = [1000,2000,1500,1200]
no_of_bedroom             = [3,5,4,3]
no_of_floor               = [1,2,1,1]
Dis_to_school             = [500,50000,1000,500]
price_list                = [100000,100000,150000,75000]
R                         = len(plinth_area)
theta_0,theta_1           = 0,0
theta_2,theta_3,theta_4   = 0,0,0
plinth_area               = Feature_Scaling(plinth_area)
no_of_bedroom             = Feature_Scaling(no_of_bedroom)
no_of_floor               = Feature_Scaling(no_of_floor)
Dis_to_school             = Feature_Scaling(Dis_to_school)

for i in range(loop):
	print("iteration:",i)
	print(theta_0,theta_1,theta_2,theta_3,theta_4)

    # To find y hat
	y_hat_list = []
	j = 0
	for i in range(R):
		y__hat = theta_0+(theta_1*plinth_area[i])+(theta_2*no_of_bedroom[i])+(theta_3*no_of_floor[i])+theta_4*Dis_to_school[i]
		y_hat_list.append(y__hat)
		j+=0
	# To find
	j = 0
	j_0__partial,j_1__partial,j_2__partial,j_3__partial,j_4__partial = 0,0,0,0,0
	for y_hat,price in zip(y_hat_list,price_list):
		j_0__partial =  j_0__partial + (y_hat_list[j]-price)
		j_1__partial =  j_1__partial + ((y_hat_list[j]-price)*plinth_area[j])
		j_2__partial =  j_2__partial + ((y_hat_list[j]-price)*no_of_bedroom[j])
		j_3__partial =  j_3__partial + ((y_hat_list[j]-price)*no_of_floor[j])
		j_4__partial =  j_4__partial + ((y_hat_list[j]-price)*Dis_to_school[j])
		j+=1
	j_0__partial = j_0__partial/R
	j_1__partial = j_1__partial/R
	j_2__partial = j_2__partial/R
	j_3__partial = j_3__partial/R
	j_4__partial = j_4__partial/R

	theta_0 = theta_0-(j_0__partial*delta)
	theta_1 = theta_1-(j_1__partial*delta)
	theta_2 = theta_2-(j_2__partial*delta)
	theta_3 = theta_3-(j_3__partial*delta)
	theta_4 = theta_4-(j_4__partial*delta)

print()

for i in range(R):
	a = plinth_area[i]
	b = no_of_bedroom[i]
	c = no_of_floor[i]
	d = Dis_to_school[i]
	Price = Price_of_a_house(a,b,c,d)
	print(Price)

			