import pandas as pd
#actividad 1
iowa_file_path = 'train.xls'
home_data = pd.read_csv(iowa_file_path)
print(home_data)
#actividad 2

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = 10517

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 13