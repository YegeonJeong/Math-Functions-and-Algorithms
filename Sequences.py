def FibonacciSequence(n):
  a = [1, 1]
  for i in range(2, n):
    a.append(a[i - 2] + a[i - 1])
  return a[n-1]

def CollatzSequence(firstterm, term):
  a = firstterm
  for j in range(term - 1):
    if a % 2 == 0:
      a /= 2
    else:
      a = 3 * a + 1
  return round(a)
