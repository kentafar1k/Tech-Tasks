d1 = {
  "srv1": {
    "cpu": "70%",
    "owner": "max_katz"
  },
  "srv2": {
    "cpu": "12%",
    "owner": "dmitry_3"
  },
  "srv3": {
    "cpu": "43%",
    "owner": "max_katz"
  }
}
# Результат парсинга
result = {
    'max_katz': [
        {'srv1': {
            'cpu': '70%'}
        },
        {'srv3': {
            'cpu': '43%'}
        }
    ],
    'dmitry_3': [
        {'srv2': {
            'cpu': '12%'}
        }
    ]
}

from functools import defaultdict

result = defaultdict(list)

for server_name, server_data in d1.items():
    owner = server_data['owner']
    result[owner].append({
        server_name: {
            'cpu': server_data['cpu']
        }
    })

# Преобразуем defaultdict обратно в обычный dict для вывода
result = dict(result)
print(result)

def curtail_str(letters: str) -> str:
    if not letters:
        return ''
    letters += '.'
    result = ''
    counter = 0
    for i in range(len(letters) - 1):
        if letters[i] != letters[i + 1]:
            if not counter:
                result += f'{letters[i]}'
            else:
                result += f'{letters[i]}{counter + 1}'
            counter = 0
        else:
            counter += 1
        print(result)

    return result


print("Hello Tochka")

assert curtail_str('') == ''
assert curtail_str("A") == "A"
assert curtail_str('ABC') == 'ABC'
assert curtail_str('AAA') == 'A3'
assert curtail_str('AAABBXYZDDDDA') == 'A3B2XYZD4A'
assert curtail_str('ABCABCABCCCCC') == 'ABCABCABC5'
print('done')