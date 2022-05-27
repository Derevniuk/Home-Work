
def create_frame(n: list, s: str):
    for i in range(len(n) + 2):
        if i == 0 or i == len(n) + 1:
            print(10 * s)
        if 0 < i < len(n) + 1:
            print(f'{s}{n[i - 1]}{" " * (8 - len(n[i - 1]))}{s}')


create_frame(['Create', 'a', 'frame'], '+')
