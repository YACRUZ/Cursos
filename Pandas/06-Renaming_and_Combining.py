import pandas as pd

##Ejercicio 1
print("===== Question 1 =====")
#Create a copy of reviews with these columns renamed to region and locale, respectively.
renamed = reviews.rename(columns=dict(region_1='region', region_2='locale'))


##Ejercicio 2
print("===== Question 2 =====")
#Set the index name in the dataset to wines.
reindexed = reviews.rename_axis('wines', axis='rows')



##Ejercicio 3
print("===== Question 3 =====")
#Create a DataFrame of products mentioned on either subreddit.
combined_products = pd.concat([gaming_products, movie_products])



##Ejercicio 4
print("===== Question 4 =====")
#Both tables include references to a MeetID, a unique key for each meet (competition) included in the database. 
left = powerlifting_meets.set_index(['MeetID'])
right = powerlifting_competitors.set_index(['MeetID'])

powerlifting_combined = left.join(right)