import pandas as pd

# select top 1 country from wine_reviews
wine_reviews = pd.read_csv("winemag-data-130k-v2.csv")

# select taster_name, taster_twitter_handle, points from wine_reviews
wine_reviews_country=wine_reviews.loc[0,'country']
print(wine_reviews_country)

# select taster_name, taster_twitter_handle, points from wine_reviews
wine_reviews2 = wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]
print(wine_reviews2)

# set title as index
wine_reviews3 = wine_reviews.set_index("title")
print(wine_reviews3)

# selct isItaly (country) from wine_reviews
is_italy=wine_reviews.country=='Italy'
print(is_italy)

# select * from wine_reviews where country is Italy
wine_reviews4=wine_reviews.loc[wine_reviews.country=='Italy']
print(wine_reviews4)

#select * from wine_reviews where country is Italy and points is 90
wine_reviews5=wine_reviews.loc[(wine_reviews.country=='Italy') & (wine_reviews.points>=90), ['country', 'points']]
print(wine_reviews5)

# select * from wine_reviews where country is Italy or points is 90
wine_reviews6=wine_reviews.loc[(wine_reviews.country=='Italy') | (wine_reviews.points>=90), ['country', 'points']]
print(wine_reviews6)

# select * from wine_reviews where country is ('Italy', 'Country')
wine_reviews7=wine_reviews.loc[~wine_reviews.country.isin(['Italy', 'France']), ['country', 'points']]
print(wine_reviews7)

wine_reviews7['points']='0'
print(wine_reviews7)

wine_reviews7['points'] = range(0, len(wine_reviews7), 1)
print(wine_reviews7)