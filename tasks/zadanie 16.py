def filter_long_words(words, n):
    return [word for word in words if len(word) > n]

# Example usage:
words = ['gigazielonyork', 'zielonyork']
filtered_words = filter_long_words(words, 10)

print(filtered_words)
