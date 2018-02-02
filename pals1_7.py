from Crypto.Cipher import AES
import base64

key = b"YELLOW SUBMARINE"
f = base64.b64decode(open('7.txt','rb').read())

cipher = AES.new(key, AES.MODE_ECB)
ans = cipher.decrypt(f)
#decode() to get the \n to print as newline
print(ans.decode())
