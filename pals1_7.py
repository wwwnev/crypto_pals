from Crypto.Cipher import AES
import base64
def decrypt_aes_ecb(b, k):
  cipher = AES.new(key, AES.MODE_ECB)
  ans = cipher.decrypt(b)
  return ans

def encrypt_aes_ecb(b, k):
  cipher = AES.new(key, AES.MODE_ECB)
  ans = cipher.encrypt(b)
  return ans


key = b"YELLOW SUBMARINE"
f = base64.b64decode(open('7.txt','rb').read())

#decode() to get the \n to print as newline
ans1 = decrypt_aes_ecb(f,key)


