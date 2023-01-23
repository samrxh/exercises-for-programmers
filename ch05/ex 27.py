import re


def validate_first_name(first_name):
    if not first_name:
        error = 'The first name must be filled in.'
    elif len(first_name) < 2:
        error = 'The first name must be at least two characters long.'
    else:
        error = None
    return error


def validate_last_name(last_name):
    if not last_name:
        error = 'The last name must be filled in.'
    elif len(last_name) < 2:
        error = 'The last name must be at least two characters long.'
    else:
        error = None
    return error


def validate_zip_code(zip_code):
    if not zip_code.isnumeric():
        error = 'The zip code must be a number.'
    else:
        error = None
    return error


def validate_employee_id(employee_id):
    x = re.search(r"[a-zA-Z]+[a-zA-Z]+[-]+\d\d\d\d", employee_id)
    if not x:
        error = 'An employee ID must have two letters, a hyphen, and four numbers.'
    else:
        error = None
    return error


def validate_input(first_name, last_name, zip_code, employee_id):
    first_name_errors = validate_first_name(first_name)
    last_name_errors = validate_last_name(last_name)
    zip_code_errors = validate_zip_code(zip_code)
    employee_id_errors = validate_employee_id(employee_id)
    validations = [first_name_errors, last_name_errors, zip_code_errors, employee_id_errors]
    errors = ''
    for item in validations:
        if item:
            errors += item + "\n"
    if errors == '':
        return 'There were no errors found.'
    return errors


# print(validate_input('J', '', 'ABCDE', 'A12-1234'))
# print(validate_input('Jimmy', 'James', '55555', 'TK-4215'))
valid = ''
while valid != 'There were no errors found.':
    first = input('Enter the first name: ')
    last = input('Enter the last name: ')
    zipc = input('Enter the zip code: ')
    emp_id = input('Enter an employee ID: ')
    print(validate_input(first, last, zipc, emp_id))
    valid = validate_input(first, last, zipc, emp_id)
