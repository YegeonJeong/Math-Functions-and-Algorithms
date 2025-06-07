def PrimeFactorization(number):
  PrimeFators = []
  num = number
  divisor = 2

  while num > 1:
    if num % divisor == 0:
      num /= divisor
      PrimeFators.append(divisor)
    else:
      divisor += 1

  return PrimeFactors
