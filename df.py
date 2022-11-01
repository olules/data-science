
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(1,10,size=(10, 3)), columns=list('ABC'))
print(df)

df['A'].values[df['A'] > 5] = 10
df['B'].values[df['A'] > 5] = 10
df['C'].values[df['A'] > 5] = 10
print(df)
