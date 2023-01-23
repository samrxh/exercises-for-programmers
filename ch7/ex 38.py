def get_evens(a):
    ls = a.split(' ')
    filter_evens(ls)
    ls = ' '.join(ls)
    return ls


def filter_evens(a):
    for item in a:
        if int(item) % 2 == 1:
            a.remove(item)
    return a


# get list of evens from user:
def get_evens_user():
    evens = get_evens(input("Enter a list of numbers, separated by spaces: "))
    print(f"The even numbers are {evens}.")


# get list of evens from file:
def get_evens_file(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if int(line) % 2 == 0]
        print(lines)


choice = input("Enter number list manually or enter from file? (manu/file) ")
if choice == 'manu':
    get_evens_user()
elif choice == 'file':
    try:
        get_evens_file(input("Enter the filename with extension. "))
    except FileNotFoundError:
        print("No such file exists.")
else:
    print("Please choose 'm' or 'f'.")
