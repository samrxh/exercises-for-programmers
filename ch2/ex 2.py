def length(string):
    if string == '':
        print("You must enter something.")
    else:
        print(f"{string} has {len(string)} characters.")


string = input("What's the input string? ")
length(string)
