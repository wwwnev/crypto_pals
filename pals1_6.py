from binascii import hexlify, unhexlify, a2b_base64, a2b_qp, a2b_uu
import pals1_3
def hamming_dist(a,b):
  return sum([bin(i ^ j).count('1') for i,j in zip(a,b)])

print(hamming_dist('this is a test'.encode('ascii'), 'wokka wokka!!!'.encode('ascii')))

f = open('6.txt','rb')
txt1 = f.read()#.replace('\n','')
txt1 = a2b_base64(txt1)

s = 110
scores2 = [(i,hamming_dist(txt1[s:s+i],txt1[s+i:s+2*i])/i) for i in range(2,41)]
scores2 = sorted(scores2, key=lambda x: x[1])
print(scores2)

for n in range(29,30):
  for i in range(0,n+1):
    txt_blc = txt1[i::n]
    #print(len(txt_blc))
    #print(n, i, pals1_3.xor_1byte(txt_blc))
    
    #print(list(filter(lambda x: int(x[2])>=0.95, pals1_3.xor_1byte(txt_blc))))

#for i in range(3):
#  for j in range(scores2[i][0]):
#    block = txt[j::scores2[i][0]]
#    if len(block)%2 == 1: block ='0' + block
#    print len(block),i,j, block
#    print filter(lambda (x,y,z): z>=0.95, pals1_3.xor_1byte(block))

