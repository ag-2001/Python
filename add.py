def calc_total(num):
    sum = 0
    for i in num:
        sum = sum + i
    return sum

def main():
    aList = []
    size = int(input("How many items would you like in your list?"))
    for i in range(size):
        newItem = input("Enter a value"):
        aList.append(int(newItem))
    print (aList)
    print(calc_total (aList)
main()


def is_even(num):
    if num % 2 == 0:
        return ("True")
    else
        return ("False")

def main():
    num = input("What is your number?")
