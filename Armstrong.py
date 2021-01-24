while(True):
    try:
        number = int(input("enter a positive integer number:"))
    except:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue
    if(number<0):
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        continue
    else:
        break

list = list(map(int, str(number)))

addition=0
for numbers in list:
    numbers**int(len(list))
    addition=numbers+addition

if(addition==number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")


