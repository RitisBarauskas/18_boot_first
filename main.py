from random import choice

NAMES = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy']

for _ in range(20):
    name = choice(NAMES)
    print(f'Hello, {name}')
