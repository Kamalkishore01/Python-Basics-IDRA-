import numpy as np

print("NumPy version:", np.__version__)
import pandas as pd

#importing the data set:
df = pd.read_csv(r"C:\Users\DELL\IDRA1st\Day7_Student_Dataset.csv")
print("Dataset loaded successfully!")

df.head()
#tops 5 rows
print("Print top 5 rows")
print(df.head(5))
#End rows
print("End rows of dataset")
print(df.tail())

print("5. Display Random Samples")
print(df.sample(5))

#Print shape of data set
print("data set shape")
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Shape of dataset:", df.shape)

#Columns
print("Columns in the dataset:")
print(df.columns)

print("Dataset Index:")
print(df.index)


#Check datatypes
print(df.dtypes)
#int64 -→ integer numbers
#float64-- → decimal numbers
#object --→ usually text/string
#bool --→ True/False values
#datetime64 → date/time values

print("Data infon: ")
print(df.info())
print("---------------------------------------------")
print("Check stats of ddatasets: ")
print(df.describe())

#
print("------------------")
print("12. Descriptive Statistics for All Columns")
print(df.describe(include="all"))

#Check null
print("______________--------------_____")
print("Check null value")
print(df.isnull().sum())

print("14. Check Whether Dataset Contains Any Missing Values ")
if df.isnull().values.any():
    print("Dataset contains missing values.")
else:
    print("No missing values found.")


print("15. Missing Values Percentage")
missing_percentage = (
    df.isnull().sum() / len(df) * 100
)
print("--------------------------------------------")
#****************************************
print("check duplicate values: ")

print("Number of duplicate rows:", df.duplicated().sum())

if df.duplicated().sum() > 0:
     print("Duplicate rows are present.")
else:
     print("No duplicate rows found.")
     
print(" 17. Check Unique Value:   ")
for column in df.columns:
    print(f"\n{column}")
    print("Unique values:", df[column].nunique())
    

print("Check memory usage:--------------------")
print(
    "Memory usage:", df.memory_usage(deep=True).sum(),
    "bytes"
)    

print("****************END**********************")
print("Summary of pandas file:          ")
print("========== DATASET SUMMARY ==========")

print("Number of Rows:", df.shape[0])
print("Number of Columns:", df.shape[1])

print("\nColumn Names:")
print(list(df.columns))

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())