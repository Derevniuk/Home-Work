import re


def count_string(file: str) -> str:
    return f'Number string: {sum(1 for line in open(file))}'


def count_words(file: str) -> str:
    with open(file, "r") as f:
        to_reading = f.read()
    numbers = len(re.sub("[,|.]", "", to_reading).split())
    return f'Number of words: {numbers}'


def count_letters(file: str) -> str:
    with open(file, "r") as f:
        to_reading = f.read()
    numbers = len(list(''.join(re.sub("[,|.]", "", to_reading))))
    return f'Number of letters: {numbers}'

print(count_string('article.txt'))
print(count_words('article.txt'))
print(count_letters('article.txt'))

