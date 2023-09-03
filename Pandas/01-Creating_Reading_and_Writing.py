import pandas as pd

##Ejercicio 1
print("===== Question 1 =====")
# In the cell below, create a DataFrame fruits
fruits = pd.DataFrame({'Apples': [30], 'Bananas': [21]})
print(fruits)



##Ejercicio 2
print("\n===== Question 2 =====")
#Create a dataframe fruit_sales
fruit_sales = pd.DataFrame([[35, 21], [41, 34]], columns=['Apples', 'Bananas'],
                index=['2017 Sales', '2018 Sales'])
print(fruit_sales)



##Ejercicio 3
print("\n===== Question 3 =====")
#Create a variable ingredients with a Series
ingredients = pd.Series(["4 cups", "1 cup", "2 large", "1 can"], index=['Flour', 'Milk', 'Eggs', 'Spam'], name='Dinner')
print(ingredients)



##Ejercicio 4
print("\n===== Question 4 =====")
#Create a variable ingredients with a Series
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv', index_col=0)
print(reviews)



##Ejercicio 5
print("\n===== Question 5 =====")
#Create a variable ingredients with a Series
animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])
animals
animals.to_csv("cows_and_goats.csv")
print(animals)