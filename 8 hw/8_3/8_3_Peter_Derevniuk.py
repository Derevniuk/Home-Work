import json

json_main = """
{
"firstName": "Alex",
"lastName": "Richardson",
"gender": "male"
}
"""

main_data = {}

data = json.loads(json_main)

data['age'] = 20
data['city'] = 'belarus'
main_data[1] = [data]


def add_human():
    g = input('Введите номер человека: ')
    main_data[g] = data
    for item in data:
        main_data[g][item] = input(f'Введите {item}: ')


add_human()

with open('data.json', 'a+') as new_json:
    json.dump(main_data, new_json)