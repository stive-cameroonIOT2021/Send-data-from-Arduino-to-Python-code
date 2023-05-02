import serial

ser=serial.Serial('com5',9600,timeout=1)
a=0
b=0
c=0
while True:
    val=ser.readline().decode('utf-8')
    parsed=val.split(',')
    parsed=[x.rstrip() for x in parsed]
    if len(parsed)>2:
        print(parsed)
        a=int(int(parsed[0]+'0')/10)
        b=int(int(parsed[1]+'0')/10)
        c=int(int(parsed[2]+'0')/10)
    print(a,b,c,a+b+c)
