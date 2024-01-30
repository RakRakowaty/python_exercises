def find_longest_word(words):
    if not words:
        return 0

    lengths = [len(word) for word in words]
    return max(lengths)

result = find_longest_word(['whyutrolling', 'papoga', 'report'])
print(result)