import pals1_3

f = open('4.txt','r')
hex_str = f.read()
print filter(lambda (x,y,z): z>=0.95, map(pals1_3.xor_1byte, hex_str.splitlines()))


