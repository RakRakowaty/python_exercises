def is_pangram(sentence):
    alphabet = set('zugzugork')
    sentence_set = set(sentence.lower())

    return alphabet.issubset(sentence_set)

# Example usage:
sentence1 = "zug zug ork bic." 
print(is_pangram(sentence1))  # Output: True

sentence2 = "zug zug!"
print(is_pangram(sentence2))  # Output: False