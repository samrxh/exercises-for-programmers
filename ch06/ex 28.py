def enter_num(loops):
    nums = []
    for _ in range(loops):
        entered = input("Enter a number: ")
        if entered.isnumeric():
            nums.append(int(entered))
        else:
            continue
    total = sum(nums)
    return total


times = int(input("How many numbers would you like to add? "))
print(f"The total is {enter_num(times)}.")
