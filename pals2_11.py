from random import randint
from pals1_7 import encrypt_aes_ecb
from pals2_9 import padding
from pals2_10 import CBC_encrypt




#tout sur cbc ou ecb? ou juste par bloc de 16?


def rand_key(n):
  ans = b''
  for i in range(n):
    ans+=bytes([randint(0,255)])
  return ans

def encryption_oracle(pt):
  key = randkey(16)
  pt = rand_key(randint(5,10)) + pt + rand_key(randint(5,10)) 
  pt = padding(pt,16)
  ct = b''
  if randint(0,1) == 0:
    ct += encrypt_aes_ecb(pt)
    print('ECB')
  else:
    iv = rand_key(16)
    ct = CBC_encrypt(pt,iv,key)
    print('CBC')

def detection_oracle():
  pt = 
