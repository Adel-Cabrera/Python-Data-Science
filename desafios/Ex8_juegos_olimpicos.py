import pandas as pd

df = pd.read_csv('athlete_events.csv')

ejercicio_1 = df.shape

print(df.loc[:, 'Games'])
print(df.loc[:, ['Games', 'NOC']])
print(df.loc[:, 'Games':'Season'])


ejercicio_2 = df['Games'].unique().size

ejercicio_3 = df[df['Season'].isin(
    ['Summer', 'Winter'])]['Season'].value_counts(normalize=True)

ejercicio_4 = df[df['Season'] == 'Summer'][df[df['Season'] == 'Summer']['Year'] == df[df['Season'] == 'Summer']['Year'].min()]['City'].unique()

ejercicio_5 = df[df['Season'] == 'Winter'][df[df['Season'] == 'Winter']['Year'] == df[df['Season'] == 'Winter']['Year'].min()]['City'].unique()

ejercicio_6 = df['NOC'].value_counts()[:10]

ejercicio_7 = df[df['Medal'].isin(
    ['Bronze', 'Silver', 'Gold'])]['Medal'].value_counts(normalize=True)

ejercicio_8 = df[df['Season'] == 'Summer'][df[df['Season'] == 'Summer']['Year'] == df[df['Season'] == 'Summer']['Year'].min()]['NOC'].unique()

print(ejercicio_1)
print(ejercicio_2)
print(ejercicio_3)
print(ejercicio_4)
print(ejercicio_5)
print(ejercicio_6)
print(ejercicio_7)
print(ejercicio_8)