import pandas as pd

# Создание DataFrame из списка словарей
data = [{'name': 'John', 'age': 30}, {'name': 'Mary', 'age': 25}]
df = pd.DataFrame(data)

print(df)

# Фильтрация данных по условию
older_than_25 = df[df['age'] > 25]
print(older_than_25)

# Группировка данных по столбцу
grouped_by_age = df.groupby('age')
print(grouped_by_age)

# Сортировка данных по столбцам
sorted_df = df.sort_values(['age'], ascending=False)
print(sorted_df)

# Агрегация данных
total_ages = df['age'].sum()
print(f"Сумма возрастов: {total_ages}")

# Сериализация данных в CSV
df.to_csv('data.csv', index=False)

# Загрузка данных из CSV
loaded_df = pd.read_csv('data.csv')
print(loaded_df)
