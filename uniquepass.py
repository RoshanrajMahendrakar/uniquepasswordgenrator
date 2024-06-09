import random as rd
length=0
ucount=1
lcount=1
scount=1
upper="ABCD"
lower="abcd"
specialsymbols="!@#$%^&*"
password=""
digits="0123456789"
while length!=10:
    if ucount!=0:
        password+=upper[rd.randint(0,len(upper)-1)]
        ucount-=1
        length+=1
    if lcount!=0:
        password+=lower[rd.randint(0,len(lower)-1)]
        lcount-=1
        length+=1
    if scount!=0:
        password+=specialsymbols[rd.randint(0,len(specialsymbols)-1)]
        scount-=1
        length+=1
    password+=digits[rd.randint(0,len(digits)-1)]    
    length+=1
print(password) 
