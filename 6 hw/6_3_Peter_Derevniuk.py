import time


def convert_second_in_time(n: int) -> str:
    return time.strftime("%H:%M:%S", time.gmtime(n))


print(convert_second_in_time(3666))
