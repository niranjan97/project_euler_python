#PROJECT EULER #2
#Find the sum of even valued terms in the fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

import math
import sys
def even_fib_sum():
    #Create fibonacci sequence using Binet's formula
    fib = []
    for i in range(100):
        if i == 0:
            fib.append(i)
        if i == 1:
            fib.append(i)
        elif fib[len(fib)-1] >= 4000000:
            break
        else:
            x_1 = (1 + math.sqrt(5))**i
            x_2 = (1 - math.sqrt(5))**i
            x_3 = (2**i) * math.sqrt(5)
            x_fin = ((x_1) - (x_2)) // x_3
            fib.append(int(x_fin))
  #Find and total all even numbers in fibonacci sequence prod   uced above
    total = 0
    for i in fib:
        if i % 2 == 0:
            total = total + i
        else:
            continue
    print(total)

even_fib_sum()
