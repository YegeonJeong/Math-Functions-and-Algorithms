def GCD(a, b):
    r = 0
    num1 = max(a, b)
    num2 = min(a, b)
    
    r = num1 % num2
    while r != 0:
        num1 = num2
        num2 = r
        r = num1 % num2
    return num2

def LCM(a, b):
  result = round(a * b / GCD(a, b))
  return result

def GCDandLCM(a, b):
  return GCD(a, b), LCM(a, b)
