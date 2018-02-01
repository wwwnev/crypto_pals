from binascii import hexlify, unhexlify, a2b_base64, a2b_qp, a2b_uu
import pals1_3
def hamming_dist(a,b):
  return sum([bin(i ^ j).count('1') for i,j in zip(a,b)])


def repeat_xor2(s, key):
  t = ''
  for i in range(len(s)):
    t += chr(ord(key[i%len(key)]) ^ s[i])
  print(t)
  return t

print(hamming_dist('this is a test'.encode('ascii'), 'wokka wokka!!!'.encode('ascii')))

f = open('6.txt','rb')
txt1 = f.read()#.replace('\n','')
txt1 = a2b_base64(txt1)

scores2 = [(i,sum([hamming_dist(txt1[s*i:s*i+i],txt1[s*i+i:s*i+2*i])/i for s in range(20)]))
    for i in range(2,41)]
scores2 = sorted(scores2, key=lambda x: x[1])
#print(scores2)


key = ''
text = []
klength = 0
for n in range(3):
  l = scores2[n][0]
  for i in range(l):
    block = txt1[i::l]
    #if len(block)%2 == 1: block ='0' + block
    #print(len(block),i,l,block)
    #print(list(filter(lambda x: float(x[2])>=0.80, pals1_3.xor_1byte(block))))
    p = pals1_3.xor_1byte(block)
    if p[2]>=0.80:
      key += p[1]
      text.append(p[0])
      klength = l

#ans = ''
#for i in range(klength):

#ans = [None] * sum([len(i) for i in text])


#ci bas: merger des strings, 1 char a la fois chaque

#for i,val in enumerate(text):
#  ans[i::klength] = val
#ans = ''.join(ans)

print(key,klength)
#print(ans)

print(repeat_xor2(txt1,key))
