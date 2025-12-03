
import random

def otpgenerate():
  for i in range(0,6):
    print(random.randint(0,9),end=' ')

otpgenerate()