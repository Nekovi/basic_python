while(True):
    number = input("enter a positive integer number:")
    if(number.isdigit() != True):
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue
    elif("-" in number):
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue
    else:
        break

addition=0
for numbers in number:
    addition=addition+(int(numbers)**len(number))

if(addition==int(number)):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")


