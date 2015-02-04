import sys

def Factorializer(number):
	if number == 1:
		return 1
	else: 
		return number*Factorializer(number-1)
print(Factorializer(int(sys.argv[1])))
