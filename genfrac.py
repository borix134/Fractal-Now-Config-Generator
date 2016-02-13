import sys,os,random
def rgb(a,b,c):
	return '#%02x%02x%02x' % (a, b, c)
def genfrac():
	os.system("rm -rf config.config")
	cfile=open("config.config", 'a')
	cfile.write("C075\n")
	typef=random.randint(1,9) #type of fractal
	if typef==1:
		cfile.write("MANDELBROT\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	elif typef==2:
		cfile.write("MANDELBROTP\n")
		cfile.write(str(random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + "\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	elif typef==3:
		cfile.write("JULIA\n")
		cfile.write(str(random.uniform(0,3)) + " " + str(random.uniform(0, 3)) + "\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	elif typef==4:
		cfile.write("JULIAP\n")
		cfile.write(str(random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + "\n")
		cfile.write(str(random.uniform(0, 3)) + " " + str(random.uniform(0, 3)) + "\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	elif typef==5:
		cfile.write("BURNINGSHIP\n")
		cfile.write(str(random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + "\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	elif typef==6:
		cfile.write("JULIABURNINGSHIP\n")
		cfile.write(str(random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + "\n")
		cfile.write(str(random.uniform(0, 3)) + " " + str(random.uniform(0, 3)) + "\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	elif typef==7:
		cfile.write("MANDELBAR\n")
		cfile.write(str(random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + "\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	elif typef==8:
		cfile.write("JULIABAR\n")
		cfile.write(str(random.uniform(0, 10)) + " " + str(random.uniform(0, 10)) + "\n")
		cfile.write(str(random.uniform(0, 3)) + " " + str(random.uniform(0, 3)) + "\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	elif typef==9:
		cfile.write("RUDY\n")
		cfile.write(str(random.uniform(0, 3)) + " " + str(random.uniform(0, 3)) + "\n")
		cfile.write(str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + " " + str(random.uniform(-2,2)) + "\n")
	cfile.write(str(random.randint(1,100000000)) + " " + "100000000\n")
	cfile.write("1\n")
	cfile.write(str(rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))) + "\n")
	if random.randint(1,2)==1:
		cfile.write("ITERATIONCOUNT\n")
		itcount=random.randint(1,3)
		if itcount==1:
			cfile.write("DISCRETE\n")
		elif itcount ==2:
			cfile.write("CONTINUOUS\n")
		else:
			cfile.write("SMOOTH\n")
	else:
		cfile.write("AVERAGECOLORING\n")
		appendfunction = random.randint(1,3)
		if appendfunction == 1:
			cfile.write("TRIANGLEINEQUALITY ")
		elif appendfunction == 2:
			cfile.write("CURVATURE ")
		else:
			cfile.write("STRIPE " + str(random.randint(1,100)) + " ")
		interpmeth=random.randint(1,3)
		if interpmeth==1:
			cfile.write("NONE\n")
		elif interpmeth==2:
			cfile.write("LINEAR\n")
		else:
			cfile.write("SPLINE\n")
		cfile.write(str(random.uniform(0,1)) + " " + str(random.uniform(0,1)) + "\n")
		cfile.write("0 " + str(rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))) + " 1 " + str(rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255))) + "\n")
i=0
while True:
	genfrac()
	i=i+1
	print ("fractals generated: " + str(i))
	raw_input()
