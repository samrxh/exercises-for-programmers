# import numpy


def get_nums():
    nums = []
    while True:
        num = input("Enter a number: ")
        if num == 'done':
            return nums
        try:
            nums.append(float(num))
        except ValueError:
            print("You must enter a number.")


def get_nums_file(filename):
    with open(filename, 'r') as nums_file:
        nums = [float(line.strip()) for line in nums_file]
        return nums


def get_mean(a):
    total = 0
    for item in a:
        total += item
    result = total / len(a)
    return result


def get_std(a):
    ls_mean = get_mean(a)
    squared_values = []
    for item in a:
        squared = (item - ls_mean) ** 2
        squared_values.append(squared)
    sv_mean = get_mean(squared_values)
    result = sv_mean ** (1/2)
    return result


# ls = get_nums()
ls = get_nums_file('ex36.txt')
# mean = numpy.mean(ls)
mean = get_mean(ls)
# std = numpy.std(ls)
std = get_std(ls)
print(mean, std)
