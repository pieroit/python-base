
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

#df_da_salvare = df[ ['Name', 'Survived', 'Fare'] ]
#df_da_salvare_order = df_da_salvare.sort_values('Fare', ascending=False)
#df_da_salvare_order.to_csv('mini_titanic.csv', sep=';', decimal=',')

def clean_survived(r):
    if r == 1:
        return 'Vivo'
    return 'Morto'

df['Survived'] = df['Survived'].map(clean_survived)
print(df['Survived'].describe())

df['Parenti'] = \
    df['Siblings/Spouses Aboard'] + df['Parents/Children Aboard']
#print(df['Parenti'].head(10))

res = df.groupby('Pclass').mean()

pivot = df.pivot_table(index=['Sex', 'Survived'], columns=['Pclass'], values='Age')
print(pivot)

plot = sns.barplot(data=df, x='Pclass', y='Fare', hue='Sex')
plt.show()

sns.countplot(data=df, x='Pclass', hue='Sex')
plt.show()

sns.scatterplot(data=df, x='Age', y='Fare', hue='Sex')
plt.show()

cc = df['Pclass'].value_counts()
cc.plot.pie()
plt.show()

#plt.show()