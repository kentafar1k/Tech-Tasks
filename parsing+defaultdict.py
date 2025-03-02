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