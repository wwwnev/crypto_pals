def padding(b ,blocksize):
  if isinstance(b, bytes) is False:
    print('Gimme bytes next time!')
    b = b.encode()
  hey = blocksize - (len(b) % blocksize)
  return b + bytes([hey]) * hey
