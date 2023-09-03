import pandas as pd

##Ejercicio 1
print("===== Question 1 =====")
# Create a Series whose index is the taster_twitter_handle category from the dataset
reviews_written = reviews.groupby('taster_twitter_handle').size()



##Ejercicio 2
print("===== Question 2 =====")
#Create a Series whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review
best_rating_per_price = reviews.groupby('price')['points'].max()



##Ejercicio 3
print("===== Question 3 =====")
#Create a DataFrame whose index is the variety category from the dataset and whose values are the min and max values thereof
price_extremes = reviews.groupby('variety').price.agg([min, max])




##Ejercicio 4
print("===== Question 4 =====")
# Create a variable sorted_varieties containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price
sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)


##Ejercicio 5
print("===== Question 5 =====")
# Create a Series whose index is reviewers and whose values is the average review score given out by that reviewer.
reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()


##Ejercicio 6
print("===== Question 6 =====")
#Create a Series whose index is a MultiIndexof {country, variety} pairs. 
country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)