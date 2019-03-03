import pandas as pd
import numpy as np

#read data sets into frames
user_ratings = pd.read_csv('../data/rating_final.csv')
cuisines = pd.read_csv('../data/chefmozcuisine.csv')

# Display 10 first rows of datasets
print(user_ratings.head(10))
print(cuisines.head(10))

# Calculate the number of ratings for each restaurant
nr_ratings = pd.DataFrame(user_ratings.groupby('placeID', as_index=False)['rating'].count(), columns=['placeID', 'rating'])
nr_ratings.sort_values('rating', ascending=False)

#extract all data for the most popular place
top_10_places = pd.DataFrame(nr_ratings.iloc[:10]['placeID'].tolist(), index=np.arange(10), columns=['placeID'])
print('top 10 places', top_10_places)

# Add cuisine type data to the table
summary = pd.merge(top_10_places, cuisines, on='placeID', how='left')
print('\n', summary)
