def is_anagram(first_word, second_word):
    if len(first_word) == len(second_word):
        ls1 = []
        ls2 = []
        for ch in first_word:
            ls1.append(ch)
        for ch in second_word:
            ls2.append(ch)
        ls1.sort()
        ls2.sort()
        if ls1 == ls2:
            print(f"'{first_word}' and '{second_word}' are anagrams.")
        else:
            print(f"'{first_word}' and '{second_word}' are not anagrams.")
    else:
        print("These words are not the same length and cannot be anagrams.")


print("Enter two strings and I'll tell you if they are anagrams.")
first = input("Enter the first string: ")
second = input("Enter the second string: ")
is_anagram(first, second)
