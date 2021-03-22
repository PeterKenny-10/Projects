import pandas as pd
import numpy as np

df = pd.read_csv("Olympic_medals.csv")

print(df.shape)

print(df.head)

print(df.info())


print(df[df.isnull().any(axis=1)])
df.dropna(axis=0,inplace=True )
print(df.shape)

hosts ={'Montreal':'Canada','Moscow':'USSR','Los Angeles':'USA', 'Soeul':'South Korea','Barcelona':'Spain','Atlanta':'USA','Sydney':'Australia','Athens':'Greece','Beijing':'China'}
for key, value in hosts.items():
    print('The host city of '+str(key)+ ' is in '+ str(value))


Ireland =df[df['Country']=='Ireland']

print(Ireland)
np_Ireland=np.array(Ireland)
print(np_Ireland.shape)




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



Ireland_sex.plot(kind='bar')
plt.title('Irelands Olympic medals male and Female', fontsize=20, color ='Green')
plt.xlabel('Year')
plt.ylabel('Medals')
plt.show()


UK_Ireland=['Ireland', 'United Kingdom']
df1= df[df['Country'].isin(UK_Ireland)]


UK_Ireland_Woman=df1.loc[df['Gender']=='Women']
UK_Ireland_Men=df1.loc[df['Gender']=='Men']
print(UK_Ireland_Woman.head())
print(UK_Ireland_Men.head())

import seaborn as sb

plt.figure(figsize=(12,5))
sb.countplot(data=df1, x='Year', hue='Gender',palette=['midnightblue','yellow'])
sb.set(style="whitegrid")
plt.legend(labels=['UK/Ireland Men','UK/Ireland Woman'],loc='center right',
           bbox_to_anchor=(1.35,0.5))
plt.title('UK and Ireland men and womens contribution in Olympics',
          fontsize=17, color ='navy')
plt.xlabel('Years', fontweight='bold', color ='navy')
plt.ylabel('Count of Athletes (woman/men', fontweight='bold', color='navy')
plt.show()

Gender_Medal= pd.DataFrame(df.groupby(['Year','Medal','Gender']).size()).reset_index()
Gender_Medal.columns = ['Year','Medal','Gender', 'Count']
(Gender_Medal.head(54))

Gender_Medal= pd.DataFrame(df.groupby(['Year','Gender','Medal']).size()).reset_index()
Gender_Medal.columns = ['Year','Gender','Medal', 'Count']
(Gender_Medal.head(54))

Male_medals= df[df['Gender']=='Men']
gender_medals_male= pd.DataFrame(Male_medals.groupby(['Year','Gender','Medal']).size()).reset_index()
gender_medals_male.columns = ['Year','Gender','Medal', 'Count']
print(gender_medals_male.head(27))

Female_medals= df[df['Gender']=='Women']
gender_medals_female= pd.DataFrame(Female_medals.groupby(['Year','Gender','Medal']).size()).reset_index()
gender_medals_female.columns = ['Year','Gender','Medal', 'Count']
print(gender_medals_female)

df_cat1= pd.concat([gender_medals_female,gender_medals_male],axis =1)
print(df_cat1)








