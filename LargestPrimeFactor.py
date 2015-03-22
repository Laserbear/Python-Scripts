#! Christian Ng
base = 0
print("Enter an integer:")
base = int(raw_input())
print "Largest Factor is:"

while (base % 2) == 0:
    base = base/2
    
if base == 1 or base == -1:
	print "2"

increment = 3

while base != 1 and base != -1: 
    
    while base % increment == 0: 
        base = base/increment
        
        
    
    increment = increment + 2

print increment - 2

