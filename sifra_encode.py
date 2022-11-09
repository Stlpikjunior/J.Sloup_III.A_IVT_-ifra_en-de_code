def sifra(ret:str,key:str):
    y = 0
    n = ''
    for i in ret:
        w = y % len(key)
        x = chr((ord(i)-97 +ord(key[w])-97)%26 +97 )
        y += 1
        n += x
    print(n)

sifra('ahojsvet','kvet')
