with open('macbeth.txt', 'r') as file:
    badger = 0
    mushroom = 0
    snake = 0
    king = 0
    for line in file:
        words = line.split()
        for item in words:
            if item == 'badger':
                badger += 1
            elif item == 'mushroom':
                mushroom += 1
            elif item == 'snake':
                snake += 1
            elif item == 'king':
                king += 1

print(f"""badger: {badger * '*'}
mushroom: {mushroom * '*'}
snake: {snake * '*'}
king: {king * '*'}""")
