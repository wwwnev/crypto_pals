from pals1_7 import encrypt_aes_ecb, decrypt_aes_ecb
from pals1_2 import fixed_xor
from pals2_9 import padding
import base64

#TODO lets make a class with that

def CBC_encrypt(pt, iv, k):
  ct = b''
  for i in range(0, len(pt), 16):
    ct_i = encrypt_aes_ecb(fixed_xor(pt[i:i+16], iv), k)
    ct = ct + ct_i
    iv = ct_i
  return ct

def CBC_decrypt(ct, iv, k):
  print(type(ct),type(iv),type(k))
  pt = b''
  for i in range(0,len(ct),16):
    print(i)
    pt_i = fixed_xor(decrypt_aes_ecb(ct[i:i+16], k), iv)
    pt = pt + pt_i
    iv = ct[i:i+16]
  return pt



f = base64.b64decode(open('10.txt','r').read())
iv = bytes([0]*16)
key = b'YELLOW SUBMARINE'

pt = CBC_decrypt(f,iv,key)
ct = CBC_encrypt(pt,iv,key)
print(f)
if ct != f: 
  print('noooooo')
#print('TWADOOOO', CBC_decrypt(f,iv,key).strip().decode('utf-8'))
