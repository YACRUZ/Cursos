print(reviews.price.dtype)

print(reviews.dtypes)

print(reviews.points.astype('float64'))

print(reviews.index.dtype)


print(reviews[pd.isnull(reviews.country)])
print(reviews.region_2.fillna("Unknown"))
print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))