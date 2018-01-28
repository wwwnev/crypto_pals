from binascii import hexlify, unhexlify
def fixed_xor(a1, a2):
  bitxor = bytes([i ^ j for i,j in zip(a1,a2)])
  bitxor = hexlify(bitxor)
  print(bitxor)
  return bitxor
#a1 = unhexlify('1c0111001f010100061a024b53535009181c')
#a2 = unhexlify('686974207468652062756c6c277320657965')
#fixed_xor(a1,a2)
