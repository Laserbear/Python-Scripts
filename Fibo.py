# Christian Ng 
import sys
def Fibo(num):
	if num <= 2:
		return 1
	else:
		return Fibo(num-1)+Fibo(num-2)
print(Fibo(int(sys.argv[1])))
