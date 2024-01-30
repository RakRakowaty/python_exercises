import re

def is_phrase_palindrome(phrase):
  
    clean_phrase = re.sub(r'[^a-zA-Z0-9]', '', phrase.lower())
    
    return clean_phrase == clean_phrase[::-1]


phrases = [
    "Go hang a salami I'm a lasagna hog.",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!"
]

for phrase in phrases:
    result = is_phrase_palindrome(phrase)
    print(f'"{phrase}" is a phrase palindrome: {result}')

