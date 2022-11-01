import os
import sys
import pandas as pd
import requests



data_Set = {
    'name': ['Jane', 'Julian', 'Fin', 'Jacob'],
    'marks': [90,80,70,50]
    
    
}
# panda series
arr = [i+1 for i in range(10)]

ps = pd.Series(arr)
print(ps[0])

df = pd.DataFrame(data_Set)
print(df)

ps = pd.Series(arr, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

# print(ps)

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
    with open('black.csv', 'wb') as f:
        f.write(r.content)
        



if not os.path.exists('black.csv'):
    download_csv(
        'https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip')


df = pd.read_csv('black.csv', engine='python-fwf'
                 )

news = pd.DataFrame(df)
print(df.head())

# Read JSON data

todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

df = pd.DataFrame(todos)

print(df.head())
