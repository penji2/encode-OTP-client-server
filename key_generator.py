import random
import string
f=open("key.dat",mode="w")
f1=open("key1.dat",mode="w")
for a in range(0,1000000):
    b=random.choice(string.ascii_letters)
    f.write(b)
    dec = ord(b)
    b = '{0:08b}'.format(dec)
    f1.write(b)

f.close()
f1.close()


