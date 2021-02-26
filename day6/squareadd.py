import math

def calculate_sum_of_squares(start,end):
    sum_of_squares = 0
    for square in range(start,end):
        sum_of_squares = sum_of_squares+pow(square,2)
    return sum_of_squares

print(calculate_sum_of_squares(1,7))