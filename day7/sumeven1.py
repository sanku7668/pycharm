#Function to calculate sum of odd numbers between 2 values
#----------------------START-------------------------------------#
def calculate_sum_of_odd_number(start,end):
    sum_of_odd_number = 0

    while end>=start:

        if(start%2!=0):
           sum_of_odd_number=sum_of_odd_number+start

        start+=1

    return sum_of_odd_number
#----------------------END-----------------------------------#


#Function to calculate sum of even numbers between 2 values

#----------------------START----------------------------------#
def calculate_sum_of_even_number(start,end):
    sum_of_even_number = 0

    while end>=start:

        if(start%2==0):
           sum_of_even_number=sum_of_even_number+start

        start+=1

    return sum_of_even_number
#----------------------END-----------------------------------#



# Main Logic here
#----------------------START-------------------------------------#
start = int(input("start wala daalo:"))
end = int(input("end wala daalo:"))

print('sum of odd numbers between ' ,start ,' and ' , end ,' is '+ str(calculate_sum_of_odd_number(start,end)))
print('sum of even numbers between ' ,start,' and ',end,' is ',str(calculate_sum_of_even_number(start,end)))
#----------------------END----------------------------------#