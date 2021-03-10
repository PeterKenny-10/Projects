import pandas as pd

df = pd.read_csv("Olympic_medals.csv")

print(df.shape)

print(df.head)

print(df.info())

brics = pd.read_csv("Olympic_medals.csv", index_col=0)
print(brics)

year_wise_total_medal= df.groupby('Year')['Medal'].count()
print(year_wise_total_medal)

year_wise_medal= df.groupby('Year')['Medal'].value_counts()
print(year_wise_medal)

year_wise_gender= df.groupby('Year')['Gender'].value_counts()
print(year_wise_gender)

Ireland =df[df['Country']=='Ireland']
print(Ireland)

Ireland_medals = Ireland.groupby('Year')['Medal'].count()
print(Ireland_medals)

Ireland_sex = Ireland.groupby('Gender')['Medal'].count()
print(Ireland_sex)


import matplotlib.pyplot as plt
Ireland_medals.plot(kind='bar')
plt.show()



year_wise_total_medal.plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Medals')
plt.show()






