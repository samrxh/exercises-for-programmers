numbers = {0}

while True:
    new_num = input("Enter a number: ")
    if new_num == 'exit':
        exit()
    int(new_num)
    numbers.add(new_num)
    max_num = 0
    for item in numbers:
        if item > max_num:
            max_num = item
    print(f"The largest number inputted so far is {max_num}.")
