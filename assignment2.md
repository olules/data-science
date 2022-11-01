# QTN 1: d
# QTN 2: 


def download_csv(url):
    r = requests.get(url)
    with open('black.csv', 'wb') as f:
        f.write(r.content)
        



if not os.path.exists('black.csv'):
    download_csv(
        'https://stats.govt.nz/assets/Uploads/Business-employment-data/Business-employment-data-June-2022-quarter/Download-data/business-employment-data-june-2022-quarter-csv.zip'
    )


df = pd.read_csv('black.csv', engine='python-fwf'
                 )

news = pd.DataFrame(df)
print(df.head())

# QTN 3.
A

# QTN 4 
df = pd.DataFrame(np.random.randint(1,10,size=(10, 3)), columns=list('ABC'))
print(df)

df['A'].values[df['A'] > 5] = 10
df['B'].values[df['A'] > 5] = 10
df['C'].values[df['A'] > 5] = 10
print(df)

# qtn 5
albums = requests.get("https://jsonplaceholder.typicode.com/albums").json()

df = pd.DataFrame(albums)

print(df.head())