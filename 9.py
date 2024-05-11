# a=int(input())
# b=int(input())
# c=a**b
# print(c)

def dar(a, b):
  if b == 0:
    return 1
  elif b < 0:
    return 1 / dar(a, -b)
  else:
    return a * dar(a, b - 1)
print(dar(2,4))