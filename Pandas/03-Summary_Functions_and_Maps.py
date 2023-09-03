import pandas as pd

##Ejercicio 1
print("===== Question 1 =====")
# What is the median of the points column in the reviews DataFrame?
median_points = reviews.points.median()
print(median_points)



##Ejercicio 2
print("===== Question 2 =====")
#hat countries are represented in the dataset? (Your answer should not include any duplicates.)
countries = reviews.country.unique()
print(countries)



##Ejercicio 3
print("===== Question 3 =====")
#How often does each country appear in the dataset?
reviews_per_country = reviews.country.value_counts()
print(reviews_per_country)



##Ejercicio 4
print("===== Question 4 =====")
#Create variable centered_price containing a version of the price column with the mean price subtracted.
centered_price = reviews.price - reviews.price.mean()
print(centered_price)



##Ejercicio 5
print("===== Question 5 =====")
#Create a variable bargain_wine with the title of the wine with the highest points-to-price ratio in the dataset.
bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']



##Ejercicio 6
print("===== Question 6 =====")
#Create a Series descriptor_counts counting how many times each of these two words appears in the description column in the dataset
tropy = reviews.description.map(lambda frut: "tropical" in frut).sum()
fruits = reviews.description.map(lambda frut: "fruity" in frut).sum()
descriptor_counts = pd.Series([tropy, fruits], index=['tropical', 'fruity'])
print(descriptor_counts)



##Ejercicio 7
print("===== Question 7 =====")
#Create a series star_ratings with the number of stars corresponding to each review in the dataset.
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')



