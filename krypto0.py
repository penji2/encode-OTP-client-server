
a=input("Message")
b=input("Password")
c=list(a)
d=list(b)
declist=[]
paslist=[]
for char in c:
    dec=ord(char)
    b = '{0:08b}'.format(dec)
    declist.append(b)

for char in d:
    dec=ord(char)
    b = '{0:08b}'.format(dec)
    paslist.append(b)


def encrypting(bitlist,password):
    encrypted =[[None for _ in range(8)] for _ in range(3)]
    encrypted1 = []
    for a in range(0,len(bitlist)):
        for b in range(0,8):
            if int(password[a][b])==1 and int(bitlist[a][b])==1 :
                encrypted[a][b]="0"
            if int(password[a][b])==1 and int(bitlist[a][b])==0:
                encrypted[a][b]="1"
            if int(password[a][b]) == 0 and int(bitlist[a][b]) == 1:
                encrypted[a][b]="1"
            if int(password[a][b]) == 0 and int(bitlist[a][b]) == 0:
                encrypted[a][b]="0"
    for a in range(0,len(bitlist)):
        c=""
        for b in range(0,8):
            c=c+encrypted[a][b]
        encrypted1.append(c)
    return encrypted1




f=(encrypting(declist,paslist))

for a in f:
    print(a)
    f=(int(a,2))
    print(chr(f))