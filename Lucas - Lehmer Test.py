def LLT(Prime):
  MersennePrime = 2 ** Prime - 1
  s = 4
  
  if Prime == 2:
    return 3 #2^2-1=3 is prime

  for i in range(1, Prime - 1):
    s = (s ** 2 - 2) % MersennePrime

  if s == 0:
    return MersennePrime
  else:
    return -1
