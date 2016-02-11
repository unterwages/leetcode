def anti_vowel(text):
    words = list(text)
    for i in text:
        if i in 'AEOIUaeoiu':
            words.remove(i)
    return ''.join(words)

print anti_vowel('wiuehfqp')
