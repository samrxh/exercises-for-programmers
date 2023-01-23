with open('ex34.txt', 'r+') as employee_list:
    employees = [line.strip() for line in employee_list]

print(employees)

print(f"There are {len(employees)} employees.")
for employee in employees:
    print(employee)

remove = input("Enter an employee name to remove: ")
if remove in employees:
    employees.remove(remove)
else:
    print("Name does not exist.")

print(f"There are {len(employees)} employees.")
for employee in employees:
    print(employee)

with open('ex34.txt', 'w') as list2:
    for item in employees:
        list2.writelines(item)
        list2.write('\n')
