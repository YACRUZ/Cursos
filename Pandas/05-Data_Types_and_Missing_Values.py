import pandas as pd

##Ejercicio 1
print("===== Question 1 =====")
#What is the data type of the points column in the dataset?
dtype = reviews.points.dtype



##Ejercicio 2
print("===== Question 2 =====")
#Create a Series from entries in the points column, but convert the entries to strings. Hint: strings are str in native Python.
point_strings = reviews.points.astype('str')



##Ejercicio 3
print("===== Question 3 =====")
#Sometimes the price column is null. How many reviews in the dataset are missing a price?
n_missing_prices = pd.isnull(reviews.price).sum()



##Ejercicio 4
print("===== Question 4 =====")
# Create a Series counting the number of times each value occurs in the region_1 field. This field is often missing data, so replace missing values with Unknown
unknow = reviews.region_1.fillna("Unknown")
reviews_per_region = unknow.value_counts().sort_values(ascending=False)