import os
import pandas as pd

data_Set = {
    'name': ['Jane', 'Julian', 'Fin', 'Jacob'],
    'marks': [90,80,70,50]
    
    
}

df = pd.DataFrame(data_Set)
print(df)


ps = pd.Series(arr, index=['a', 'b', 'c'])

print(ps['a'])


calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390,
    "day4": 420,
}


p_calories = pd.Series(calories)
print(p_calories)

# Locate a row

df = pd.DataFrame(calories, index=['day1', 'day2', 'day3', 'day4'])
print(df.loc['day2'])

# Load CSV


def download_csv(url):
    r = requests.get(url)
    with open('data.csv', 'wb') as f:
        f.write(r.content)


if not os.path.exists('data.csv'):
    download_csv(
        'https://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv')


df = pd.read_csv('data.csv')
print(df)

df = pd.read_csv('bands.csv')
print(df.head())

# Read JSON data

todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

df = pd.DataFrame(todos)

print(df.head())
