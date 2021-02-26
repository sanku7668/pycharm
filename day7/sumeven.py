
#indentation matters bro
#jis level pe function likha usi level pe ye bahar ka code hai

def calculate_sum_of_even_number(start,end):
    sum_of_even_number = 0
    while end>=start:
        #while ke andar ka code
        if(start%2==0):
            #if ke andar ka code
           sum_of_even_number=sum_of_even_number+start
            #if khatam ab wapis while chalu aage ka
    #jo while ke andar hai wo while ke thoda saamne
        #ye bhi while ke andar ka code
        start+=1
        #while khatam
        #while khatam , ab function calculate_sum_of_even_number ke level pe aaye
    return sum_of_even_number

#bahara ka code
print(calculate_sum_of_even_number(1,10))


def calculate_sum_of_odd_number(start,end):
    sum_of_odd_number = 0

    while end>=start:

        if(start%2!=0):
           sum_of_odd_number=sum_of_odd_number+start

        start+=1

    return sum_of_odd_number
print(calculate_sum_of_odd_number(1,10))