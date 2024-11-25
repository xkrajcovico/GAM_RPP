def vowel_count(word):
    s = set(word)
    vowels = 0
    for char in s:
        if char in 'aeiouy':
            vowels += 1
    print(vowels)
vowel_count('vowel_count') 