

def encrypting(bitlist, password):
    encrypted = [[None for _ in range(8)] for _ in range(len(bitlist))]
    encrypted1 = []
    for a in range(0, len(bitlist)):
        for b in range(0, 8):
            if int(password[a][b]) == 1 and int(bitlist[a][b]) == 1:
                encrypted[a][b] = "0"
            if int(password[a][b]) == 1 and int(bitlist[a][b]) == 0:
                encrypted[a][b] = "1"
            if int(password[a][b]) == 0 and int(bitlist[a][b]) == 1:
                encrypted[a][b] = "1"
            if int(password[a][b]) == 0 and int(bitlist[a][b]) == 0:
                encrypted[a][b] = "0"
    for a in range(0, len(bitlist)):
        c = ""
        for b in range(0, 8):
            c = c + encrypted[a][b]
        encrypted1.append(c)
    return encrypted1

def decrypting(bitlist,password):
    bitlist=list(bitlist)
    password=list(password)
    encrypted=[None]*len(bitlist)
    encrypted1 = [[None for _ in range(8)] for _ in range(int(len(encrypted)/8))]
    encrypted2=[]
    for a in range(0, len(bitlist)):
        if int(password[a]) == 1 and int(bitlist[a]) == 1:
            encrypted[a]="0"
        if int(password[a]) == 1 and int(bitlist[a]) == 0:
            encrypted[a]="1"
        if int(password[a]) == 0 and int(bitlist[a]) == 1:
            encrypted[a]="1"
        if int(password[a]) == 0 and int(bitlist[a]) == 0:
            encrypted[a]="0"

    for d in range(0,int(len(encrypted)/8)):
        c=0
        for a in encrypted:
            encrypted1[d][c]=a
            print(d,c,a)
            c+=1
            if c==8:
                break
    for a in range(0, int(len(encrypted)/8)):
        c = ""
        for b in range(0, 8):
            c = c + encrypted1[a][b]
        encrypted2.append(c)

    return encrypted2

def main(mes,pas):
    a = mes
    b = pas
    c = list(a)
    d = list(b)
    declist = []
    paslist = []
    for char in c:
        dec = ord(char)
        b = '{0:08b}'.format(dec)
        declist.append(b)
    for char in d:
        dec = ord(char)
        b = '{0:08b}'.format(dec)
        paslist.append(b)
    f = encrypting(declist, paslist)
    x = encrypting(f, paslist)
    encmessage=[]
    y=''
    for a in f:
        y+=a
    for a in x:
        x = (int(a, 2))


    for a in f:
        f = (int(a, 2))
        encmessage.append(chr(f))


    return y
