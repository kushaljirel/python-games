import random

def jumble(word): 
    # sample() method shuffling the characters of the word 
    random_word = random.sample(word, len(word)) 
  
    # join() method join the elements 
    # of the iterator(e.g. list) with particular character . 
    jumbled = ''.join(random_word) 
    return jumbled 
# print(jumble("apple"))
variable = str(input("Enter the name to mix: "))
mix  = random.sample(variable,  len(variable))
mixed = "".join(mix)
# print(mixed)


