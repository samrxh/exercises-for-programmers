with open('ex41_out.txt', 'w') as file_out:
    with open('ex41_in.txt', 'r+') as file_in:
        names = [line.strip() for line in file_in]
        names.sort()
        print(f"Total of {len(names)} names:")
        for name in names:
            file_out.write(name + '\n')