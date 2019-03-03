import pandas as pd
import numpy as np

user_ratings = pd.read_csv('../data/rating_final.csv')
cuisines = pd.read_csv('../data/chefmozcuisine.csv')
geodata = pd.read_csv("../data/geoplaces.csv", encoding='latin')
places = geodata[['placeID', 'name']]

#subset geodata by extracting only placeID and name with place name columns
print(user_ratings.head())
print(geodata.head())
print(places.head())

ratings = pd.DataFrame(user_ratings.groupby('placeID')['rating'].mean())
ratings['rating_count'] = pd.DataFrame(user_ratings.groupby('placeID')['rating'].count())

print(ratings.sort_values('rating_count', ascending=False).head())

#print top place row in places
print(places[places['placeID']==135085])
print(cuisines[cuisines['placeID']==135085])

#Prepare the data, user by item
places_rating_crosstab = pd.pivot_table(data=user_ratings, values='rating', index='userID', columns='placeID')

print(places_rating_crosstab.head())

tortas_ratings = places_rating_crosstab[135085]
tortas_ratings[tortas_ratings>=0]

#Evaluating similarity based on Correlation

similar_to_tortas = places_rating_crosstab.corrwith(tortas_ratings)
corr_tortas = pd.DataFrame(similar_to_tortas, columns=['PearsonR'])
#drop all null values
corr_tortas.dropna(inplace=True)
corr_tortas = corr_tortas.sort_values('PearsonR', ascending=False)
print(corr_tortas.head())

tortas_corr_summary = corr_tortas.join(ratings['rating_count'])

# print only those places that correlate with tortas that have more than 10 ratings
print(tortas_corr_summary[tortas_corr_summary['rating_count']>=10].head(10))

#throw out places that have only 1 reviewer, the places need to have at least 2 reviewers.
top_corr_places_tortas = pd.DataFrame([135085, 132754, 135045, 135062, 135028, 135042, 135046], index=np.arange(7), columns=['placeID'])

#left join
summary = pd.merge(places_corr_tortas, cuisines, on='placeID', how='left')
summary
