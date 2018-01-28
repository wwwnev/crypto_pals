import binascii
def hex_b64(a):
  b = binascii.a2b_hex(a)
  a_b64 = binascii.b2a_base64(b)
  return a_b64

#a = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
#a_b64 = hex_b64(a)
#print a_b64
