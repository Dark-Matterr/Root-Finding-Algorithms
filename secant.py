import math

# Edit the function/equation here
def func(x):
	return math.pow(x, 3)-(2*math.pow(x, 2))+x-1

def xNew(x, y):
	return x-((func(x)*(x-y))/(func(x)-func(y)))

def recurrence(x, y, err):
	if err >= abs(x-y):
		print("["+str(x)+", "+str(y)+", "+str(func(x))+", "+str(func(y))+", "+str(xNew(x, y))+"] = Error > "+str(abs(xNew(x, y) - y)))
		return y
	print("["+str(x)+", "+str(y)+", "+str(func(x))+", "+str(func(y))+", "+str(xNew(x, y))+"] = Error > "+str(abs(xNew(x, y) - y)))
	return recurrence(y, xNew(x, y), err)



x = float(input("Enter your X0: "))
y = float(input("Enter your X1: "))
e = float(input("Error: "))
print("---------------------\nThe approximated root: "+str(recurrence(x, y, e)))
