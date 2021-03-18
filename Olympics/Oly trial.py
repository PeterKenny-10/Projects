import pandas as pd

df = pd.read_csv("Olympic_medals.csv")

print(df.shape)

print(df.head)

print(df.info())

print(df[df.isnull().any(axis=1)])
df.dropna(axis=0,inplace=True )
print(df.shape)




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
plt.title('Irelands Olympic medals',fontsize=18, color='red')
plt.xlabel('Year')
plt.ylabel('Medals')
plt.show()



year_wise_total_medal.plot(kind='bar')
plt.xlabel('Year')
plt.ylabel('Medals')
plt.show()

United_States = df[df['Country']== 'United States']
United_States_medals = United_States.groupby('Year')['Medal'].count()


Spain = df[df['Country']== 'Spain']
Spain_medals = Spain.groupby('Year')['Medal'].count()


hosts ={'Montreal':'Canada','Moscow':'USSR','Los Angeles':'USA', 'Soeul':'South Korea','Barcelona':'Spain','Atlanta':'USA','Sydney':'Australia','Athens':'Greece','Beijing':'China'}
for key, value in hosts.items():
    print('The host city of '+str(key)+ ' is in '+ str(value))

print(df.iloc[10000:10050,1:4])

UK_Ireland=['Ireland', 'United Kingdom']
df1= df[df['Country'].isin(UK_Ireland)]

UK_Ireland_Woman=df1.loc[df['Gender']=='Women']
UK_Ireland_Men=df1.loc[df['Gender']=='Men']
print(UK_Ireland_Woman.head())
print(UK_Ireland_Men.head())

plt.figure(figsize=(12,5))
plt.legend(labels=['UK/Ireland Men', 'Uk/Ireland Woman'])
plt.xlabel('Years')
plt.ylabel('Count of Athletes (Women/Men')
plt.show()








