def word_lengths(word_list):
    return [len(word) for word in word_list]

words = ["Ork", "zebra", "pomarzancza", "kiwi"]
lengths = word_lengths(words)

print(lengths)