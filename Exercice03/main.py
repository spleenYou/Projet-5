words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowels = ["a", "e", "i", "o", "u", "y"]
comprehension_list = []
for word in words:
    number_or_vowels = 0
    for vowel in vowels:
        number_or_vowels = number_or_vowels + word.count(vowel)
    comprehension_list.append((word, number_or_vowels))
print(comprehension_list)
