import pals1_3
import binascii
#rb sans unhexlify ne fonctionne pas
f = open('4.txt','r')
sc = filter(lambda x: x[2] > 0.95, [pals1_3.xor_1byte(binascii.unhexlify(i.strip())) for i in f])
print(list(sc))

