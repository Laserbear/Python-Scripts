from os import urandom
 
def keygen(length):

    return urandom(length)
 
def xor_strings(s,t):
  
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))
 
 
message = raw_input()
print 'message:', message
 
key = keygen(len(message))
print 'key:', key
 
cipherText = xor_strings(message, key)
print 'cipherText:', cipherText
print 'decrypted:', xor_strings(cipherText,key)
 

if xor_strings(cipherText, key) == message:
    print 'Success'


