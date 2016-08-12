# Count number of uppercase and lower case letter in a word


def letter_count(word):
    uppercase_letter = 0
    lowercase_letter = 0
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in word:
        if letter in letters:
            lowercase_letter += 1
        else:
            uppercase_letter += 1
    return [uppercase_letter, lowercase_letter]

if __name__ == '__main__':
    word = 'HizBulBahaR'
    print(letter_count(word))
