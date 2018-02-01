from binascii import hexlify, unhexlify
def score_str(a):
  l = len(a)
  ll = len(list(filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z' or x==' ', a)))
  return ll/l

#a is bytes
def xor_1byte(a):
  top = 0
  top_key = ''
  top_str = ''
  for i in range(256):
    b = map(chr,[i ^ j for j in a])
    b = ''.join(b)
    scr = score_str(b)
    if scr > top: 
      top = scr
      top_key = chr(i)
      top_str = b
  #print(type(top),top)
  return(top_str, top_key, top)
#a = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
#ans = xor_1byte(a)
#print(ans)
#print(xor_1byte(ans[0].encode('ascii')))
