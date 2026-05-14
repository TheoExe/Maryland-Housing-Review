# Theophilus Braimoh 1-28-2026
# Python Script to analysis MD Housing Rehab Program CSV file

import pandas

house = pandas.read_csv("Maryland_Housing_Rehab_Special_Loans_Program_FY_2011-2023.csv")

# print(house.head(5))


house.describe()
