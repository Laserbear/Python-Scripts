import sys

 
def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

 
def printAscii(msg):
    z = [chr(ord(x)) for x in msg] 
    x = "".join(z)
    print x.encode('hex')
 
def main():
    text = "attack at dawn"
  
    
    enc = "6c73d5240a948c86981bc294814d".decode('hex')
    key = strxor(text, enc)
 
 
    text2 = "attack at dusk"
    enc2 = strxor(text2, key)
 
    print enc2.encode('hex')
 
 
 
main()
