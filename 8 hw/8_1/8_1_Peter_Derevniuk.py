import re


def longest_words(file: str) -> str:
    with open(file, "r") as f:
        to_reading = f.read()
    s = re.sub("[,|.]", "", to_reading)
    return max(s.split(), key=len)


print(longest_words('article.txt'))
