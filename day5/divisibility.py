number = input ("write a number: ")

if(int(number) % 3 == 0) and (int(number) % 5 == 0):
    print("number is divisible by both")


elif(int(number) % 3 == 0):
     print("number is divisible by 3")
 

    
elif(int(number) % 5 == 0):
     print("number is divisible 5")


else:
     print("number is not divisible by both")

