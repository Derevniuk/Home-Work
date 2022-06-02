import re

with open("article.txt", "r") as f:
    to_reading = f.read()


def longest_words(file: str) -> str:
    s = re.sub("[,|.]", "", file)
    return max(s.split(), key=len)


print(longest_words(to_reading))
