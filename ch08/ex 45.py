with open('ex45.txt', 'r+') as f:
    new_text = ''
    for line in f:
        line.strip()
        new_line = line.replace('utilize', 'use')
        new_text += new_line
    new_file = input("What would you like to name the new file? ")
    new_file = f'{new_file}.txt'
    with open(new_file, 'w') as output:
        output.write(new_text)
