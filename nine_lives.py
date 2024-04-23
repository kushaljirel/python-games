import random
heart = u'\u2764'
words = [
    "air", "eye"
]

secret_word = random.choice(words)
# print(secret_word)
clue = list("???")
# print(clue)
# secret_word = list(secret_word) 
# print(secret_word)
guessed_word_correctly = False
lives = 9
def update_clue(clue, guessed_letter, secret_word):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1    


while lives>0:
    print(clue)
    print("lives left: " + heart*lives)
    guess = input("Enter the guess letter: ")

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(clue, guess, secret_word)
    else:
        print("wrong!!! try again")
        lives = lives - 1    


if guessed_word_correctly:
    print('u win')
else:
    print("u lose")
'''
print(secret_word)
secret_word[1] = "2"
print(secret_word)
'''