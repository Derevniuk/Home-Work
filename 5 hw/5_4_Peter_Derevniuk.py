import random
import json


def random_list(n):
    return [random.randint(1, 40) for i in range(n)]


def res_number(n):
    c = random_list(n)
    return {i: c.count(i) for i in set(c) if c.count(i) > 1}


def data_output(n):
    return json.dumps(res_number(n), indent=4, sort_keys=True)


print(data_output(20))
