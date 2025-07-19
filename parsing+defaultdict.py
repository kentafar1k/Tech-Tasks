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
