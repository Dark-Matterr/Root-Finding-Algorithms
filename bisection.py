import math

# Edit the function/equation here
def func(x):
	return math.pow(x, 6)-x-1

def midpoint(a, b):
	return (a+b)/2

def sign(num):
	if num >= 0:
		return "+"
	elif num < 0:
		return "-"

def converge_iter(a, b, n):
	return (abs(b - a)/math.pow(2, n))


def recurrence(a, mid, b, err, prev_mid=0, iter=1):
	if err >= abs(prev_mid - mid):
		print("["+str(a)+", "+str(b)+", "+str(func(a))+", "+str(func(b))+" , "+str(mid)+", "+str(func(mid))+", "+str(converge_iter(a, b, iter))+"] = Error < "+ str(abs(prev_mid - mid)))
		return mid
	elif (sign(func(mid))  != sign(func(a))):
		print("["+str(a)+", "+str(b)+", "+str(func(a))+", "+str(func(b))+" , "+str(mid)+", "+str(func(mid))+", "+str(converge_iter(a, b, iter))+"] = Error < "+ str(abs(prev_mid - mid)))
		return recurrence(a, midpoint(a, mid), mid, err, mid, iter+1)
	else:
		print("["+str(a)+", "+str(b)+", "+str(func(a))+", "+str(func(b))+" , "+str(mid)+", "+str(func(mid))+", "+str(converge_iter(a, b, iter))+"] = Error < "+ str(abs(prev_mid - mid)))
		return recurrence(mid, midpoint(mid, b), b, err, b, iter+1)
		

a = int(input("Bracket A: "))
b = int(input("Bracket B: "))
e = float(input("Error: "))
#debugging
print("---------------------\nThe approximated root: "+str(recurrence(a, midpoint(a, b), b, e)))