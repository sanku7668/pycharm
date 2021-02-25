def calculate_square(input):
    sqrt_i =input*input
    return sqrt_i

def just_print_name():
    print("sanku")

def calculate_sum_of_squares(start,end):
    sum_of_squares = 0
    while end>=start:
        sum_of_squares = sum_of_squares+(start*start)
        start+=1
    return sum_of_squares


#print(calculate_square(5))
#just_print_name()

# 1 + 2*2 + 3*3 = 14
#print(calculate_sum_of_squares(1,3))

# 1 + 2*2 + 3*3 +4*4 = 30
#print(calculate_sum_of_squares(1,4))

# 1 + 2*2 + 3*3 +4*4 +5*5= 55
print(calculate_sum_of_squares(1,5))
    
