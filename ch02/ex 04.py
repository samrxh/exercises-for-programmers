def gather_word(word_type, amount=1):
    word_list = []
    for item in range(amount):
        if word_type[0] == 'a':
            word = input(f'Enter an {word_type}: ')
        else:
            word = input(f'Enter a {word_type}: ')
        word_list.append(word)
    for item in word_list:
        return item


# def gather_words(nouns, verbs, adjectives, adverbs):
#     noun_list = gather_word(nouns, 'noun')
#     verb_list = gather_word(verbs, 'verb')
#     adj_list = gather_word(adjectives, 'adjective')
#     adv_list = gather_word(adverbs, 'adverb')


noun = gather_word('noun')
verb = gather_word('verb')
adjective = gather_word('adjective')
adverb = gather_word('adverb')

print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious! {noun}")

# Challenges:
# Add more inputs to the program to expand the story.
# Implement a branching story, where the answers to questions determine how the story is constructed.