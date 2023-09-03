import pandas as pd

##Ejercicio 1
print("===== Question 1 =====")
# Select the description column from reviews and assign the result to the variable desc.
desc = reviews.description
print(desc)



##Ejercicio 2
print("\n===== Question 2 =====")
#Select the first value from the description column of reviews, assigning it to variable first_description
first_description = reviews['description'][0]
print(first_description)



##Ejercicio 3
print("\n===== Question 3 =====")
#Select the first row of data (the first record) from reviews, assigning it to the variable first_row.
first_row = reviews.iloc[0]
print(first_row)



##Ejercicio 4
print("\n===== Question 4 =====")
#Select the first 10 values from the description column in reviews, assigning the result to variable first_descriptions.
first_descriptions = reviews['description'][:10]
print(first_descriptions)



##Ejercicio 5
print("\n===== Question 5 =====")
#Select the records with index labels 1, 2, 3, 5, and 8, assigning the result to the variable sample_reviews.
num=[1,2,3,5,8]
sample_reviews = reviews.loc[num]
print(sample_reviews)



##Ejercicio 6
print("\n===== Question 6 =====")
#Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels 0, 1, 10, and 100
col = ['country', 'province', 'region_1', 'region_2']
num = [0, 1, 10, 100]
df = reviews.loc[num, col]
print(df)




##Ejercicio 7
print("\n===== Question 7 =====")
#Create a variable df containing the country and variety columns of the first 100 records.
col = ['country', 'variety']
df = reviews.loc[:99, col]
print(df)



##Ejercicio 8
print("\n===== Question 8 =====")
#Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines = reviews[reviews.country == 'Italy']
print(italian_wines)



##Ejercicio 9
print("\n===== Question 9 =====")
#Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]
print(top_oceania_wines)