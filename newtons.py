import math

# Edit the function/equation here
def func(x):
	return math.pow(math.e, -1*(x))-x

def derivative(x):
	return -1*math.pow(math.e, -1*(x))-1


def xNew(o, f, d):
	return o-(f/d)

def recurrence(x, err, prev_x=0):
	if err >= abs(prev_x - x):
		print("["+str(x)+", "+str(func(x))+", "+str(derivative(x))+" , "+str(xNew(x, func(x), derivative(x)))+"] = Error > "+str(abs(xNew(x, func(x), derivative(x)) - x)))
		return x
	print("["+str(x)+", "+str(func(x))+", "+str(derivative(x))+" , "+str(xNew(x, func(x), derivative(x)))+"] = Error > "+str(abs(xNew(x, func(x), derivative(x)) - x)))
	return recurrence(xNew(x, func(x), derivative(x)), err, x)


x = int(input("Enter your X0: "))
e = float(input("Error: "))
print("---------------------\nThe approximated root: "+str(recurrence(x, e)))