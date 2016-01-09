#POJECT EULER #1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. Sum of multiples is 23. 

#Find sum of all multiples of 3 or 5 below 1000. 

def sum_of_multiples():
    multiples = []
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            multiples.append(i)
        else:
            continue
    total = 0
    for i in multiples:
        total = total + i
    print(total)

sum_of_multiples()
