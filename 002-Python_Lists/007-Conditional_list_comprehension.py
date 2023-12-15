a = [-1, 10, -20, 2, -90, 60, 45, 20]
b = [item**2 for item in a if item < 0]
print(b)

sentence = "The quick brown fox jumps over the lazy dog"


def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels


consonants = [i for i in sentence if is_consonant(i)]
print(consonants)

c = [-1, 10, -20, 2, -90, 60, 45, 20]
d = [i if i > 0 else 0 for i in c]
print(d)


def get_number(number):
    return number if number > 0 else "negative number"


e = [get_number(i) for i in c]
print(e)
