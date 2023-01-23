with open('ex53.txt', 'r+') as f:
    task = None
    while task != '':
        task = input("Enter a task to add to your to-do list: ")
        if task:
            f.write(task + '\n')
    print("Here are your tasks:")
    f.seek(0)
    for line in f:
        print(line)
    f.seek(0)
    remove = None
    while remove != '':
        remove = input("Enter a task you would like to remove: ")
        for line in f:
            line = line.replace(remove, '')
        f.seek(0)
