#PROJECT EULER 6

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum .


def sum_square_diff():
    total = 0
    for i in range(1, 101):
        total = (i**2) + total
    print(total)
    temp = 0
    for i in range(1, 101):
        temp = i + temp
    print(total - (temp**2))


sum_square_diff()
