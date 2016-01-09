#PROJECT EULER 4

#Find largest palindromic number made from the product of two three digit numbers

def palin_finder():
    num_list = []
    for i in range(100, 1000):
        for x in range(100, 1000):
            y = i * x
            y_int = [int(i) for i in str(y)]
            if y_int == y_int[::-1]:
                num_list.append(y)
            else:
                continue
    print(max(num_list))

palin_finder()
