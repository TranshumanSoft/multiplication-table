number = int(input("What is the number that you want to know its multiplication table?"))
counter = 0
while True:
    counter = counter + 1
    table = counter * number
    print(f"{number} * {counter} = {table}")
    if counter == 10:
        break
print(f"This is the table of {number}")