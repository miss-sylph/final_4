import pandas as pd

# Загружаем данные из CSV файла
data = pd.read_csv('data.csv')

# 1. Вычисляем среднюю зарплату всех сотрудников
average_salary = data['salary'].mean()
print(f"Средняя зарплата: {average_salary:.2f}")

# 2. Выбираем сотрудников старше 30 лет
older_than_30 = data[data['age'] > 30]

# 3. Выводим сотрудников старше 30 лет
print("\nСотрудники старше 30 лет:")
print(older_than_30[['name', 'age', 'salary']])

