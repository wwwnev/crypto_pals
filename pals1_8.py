from collections import Counter
from Crypto.Cipher import AES

#TODO smart decision to choose the most probably aes ecb ciphertext rather than list all possibilities. Threshold?

def maybe_aesecb(c,idx):
  for i in range(4,17):
    lst = [c[j:j+i] for j in range(0,len(c),i)]
    counter = list(filter(lambda x: x!= 1, Counter(lst).values()))
    if len(counter) > 0:
      print('idx: ',idx, ' block length: ', i, ' VALEURS: ', counter)

f = open('8.txt','rb').read().splitlines()

for idx,stf in enumerate(f):#len(f)-16):
  maybe_aesecb(stf,idx)
