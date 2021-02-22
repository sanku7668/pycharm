try:
    answer = 10/0
    number = int(input("enter a number: "))
    print(number)
except ZerodivisionError as err:
    print(err)
except Valueerror:
    print("invalid input")
