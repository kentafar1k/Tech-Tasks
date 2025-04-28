statistics_1 = [
    [{ 'userId': 1, 'steps': 1000 }, { 'userId': 2, 'steps': 1500 }],
    [{ 'userId': 2, 'steps': 2000 }],
    [{ 'userId': 1, 'steps': 3000 }]
]

# Ожидаемый вывод
champions = { 'userIds': [1], 'steps': 4000 }


statistics_2 = [
    [{ 'userId': 1, 'steps': 2000 }, { 'userId': 2, 'steps': 1500 }],
    [{ 'userId': 2, 'steps': 4000 }, { 'userId': 1, 'steps': 3500 }],
    []  # Простой день (пропуск одного дня)
]

# Ожидаемый вывод
champions = { 'userIds': [1, 2], 'steps': 5500 }


