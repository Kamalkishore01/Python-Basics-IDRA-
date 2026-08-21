# CLEANED COMPANY EMPLOYEE DATASET - DAY 11
# Python + Pandas


import pandas as pd
import numpy as np


# ============================================================
# 1. LOAD DATASET

df = pd.read_csv("Day11_Messy_Company_Employee_Dataset.csv")

print("=" * 60)
print("COMPANY EMPLOYEE DATASET - BEFORE CLEANING")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())


# ======================
# 2. INSPECT DATASET
# ===================

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()

print("\nStatistical Summary:")
print(df.describe())


# ============================================================
# 3. CHECK MISSING VALUES

print("\n" + "=" * 60)
print("MISSING VALUES BEFORE CLEANING")
print("=" * 60)

missing_values = df.isnull().sum()

print(missing_values)

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nMissing Value Percentage:")
print(
    (df.isnull().sum() / len(df) * 100)
    .round(2)
)


# ========================
# 4. CHECK DUPLICATE RECORDS
# =====================

print("\n" + "=" * 60)
print("DUPLICATE RECORDS BEFORE CLEANING")
print("=" * 60)

duplicate_count = df.duplicated().sum()

print("Number of duplicate rows:", duplicate_count)


# 5. CHECK UNIQUE / INCONSISTENT VALUES
# ============================================================
print("\n" + "=" * 60)
print("INCONSISTENT CATEGORICAL VALUES")
print("=" * 60)

print("\nDepartment values:")
print(df["Department"].value_counts(dropna=False))

print("\nGender values:")
print(df["Gender"].value_counts(dropna=False))

print("\nCity values:")
print(df["City"].value_counts(dropna=False))

print("\nWork Mode values:")
print(df["Work_Mode"].value_counts(dropna=False))


# =====================
# 6. CHECK DATA TYPES
# ====================

print("\n" + "=" * 60)
print("DATA TYPES BEFORE CLEANING")
print("=" * 60)

print(df.dtypes)


# ============================================================
# 7. REMOVE EXTRA SPACES FROM COLUMN NAMES

df.columns = df.columns.str.strip()


# ============================================================
# 8. CLEAN TEXT / CATEGORICAL COLUMNS

# Remove leading/trailing spaces
text_columns = [
    "Employee_ID",
    "Employee_Name",
    "Department",
    "Job_Title",
    "Gender",
    "City",
    "Work_Mode"
]

for column in text_columns:
    df[column] = df[column].str.strip()


# Convert inconsistent text to consistent format

# Department
df["Department"] = df["Department"].str.title()
# Gender
df["Gender"] = df["Gender"].str.title()
# City
df["City"] = df["City"].str.title()

# Work Mode
df["Work_Mode"] = df["Work_Mode"].str.title()


# =========================================
# 9. CHECK CATEGORICAL VALUES AFTER STANDARDIZATION
# =================================

print("\n" + "=" * 60)
print("CATEGORICAL VALUES AFTER STANDARDIZATION")
print("=" * 60)

print("\nDepartment:")
print(df["Department"].value_counts(dropna=False))

print("\nGender:")
print(df["Gender"].value_counts(dropna=False))

print("\nCity:")
print(df["City"].value_counts(dropna=False))

print("\nWork Mode:")
print(df["Work_Mode"].value_counts(dropna=False))


# ============================================================
# 10. CONVERT DATA TYPES

# Numeric columns
numeric_columns = [
    "Age",
    "Annual_Salary",
    "Experience_Years",
    "Performance_Score"
]

for column in numeric_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"    )


# Convert Joining_Date to datetime
df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    errors="coerce"
)


# ============================================================
# 11. CHECK DATA TYPES AFTER CONVERSION

print("\n" + "=" * 60)
print("DATA TYPES AFTER CONVERSION")
print("=" * 60)

print(df.dtypes)


# ================================
# 12. HANDLE MISSING VALUES

print("\n" + "=" * 60)
print("HANDLING MISSING VALUES")
print("=" * 60)


# ------------------------------------------------------------
# Department
# Categorical column -> use MODE

department_mode = df["Department"].mode()[0]

df["Department"] = df["Department"].fillna(
    department_mode
)

print(
    "Department missing values filled with mode:",
    department_mode
)


# ---------------------------------------------------
# Gender
# Categorical column -> use MODE
# --------------------

gender_mode = df["Gender"].mode()[0]

df["Gender"] = df["Gender"].fillna(
    gender_mode
)

print(
    "Gender missing values filled with mode:",
    gender_mode
)


# ------------------------------------------------------------
# City
# Categorical column -> use MODE
# ------------------------

city_mode = df["City"].mode()[0]

df["City"] = df["City"].fillna(
    city_mode
)

print(
    "City missing values filled with mode:",
    city_mode
)


# ------------------------------------------------------------
# Work Mode
# Categorical column -> use MODE

work_mode = df["Work_Mode"].mode()[0]

df["Work_Mode"] = df["Work_Mode"].fillna(
    work_mode
)

print(
    "Work Mode missing values filled with mode:",
    work_mode
)


# ------------------
# Age
# Numerical column -> use MEDIAN

age_median = df["Age"].median()

df["Age"] = df["Age"].fillna(
    age_median
)

print(
    "Age missing values filled with median:",
    age_median
)


# ------------------------------------------------
# Annual Salary
# Numerical column -> use MEDIAN

salary_median = df["Annual_Salary"].median()

df["Annual_Salary"] = df["Annual_Salary"].fillna(
    salary_median
)

print(
    "Annual Salary missing values filled with median:",
    salary_median
)


# ----------------------
# Experience
# Numerical column -> use MEDIAN

experience_median = df["Experience_Years"].median()

df["Experience_Years"] = df["Experience_Years"].fillna(
    experience_median
)

print(
    "Experience missing values filled with median:",
    experience_median
)


# ------------------------------------------------------------
# Performance Score
# Numerical column -> use MEDIAN

performance_median = df["Performance_Score"].median()

df["Performance_Score"] = df["Performance_Score"].fillna(
    performance_median
)

print(
    "Performance Score missing values filled with median:",
    performance_median
)


# ============================================================
# 13. DEMONSTRATE FORWARD FILLING

# Forward filling is useful for ordered/sequential data.
# We demonstrate it on Joining_Date after sorting by Employee_ID.

df = df.sort_values(
    by="Employee_ID"
).reset_index(drop=True)

df["Joining_Date"] = df["Joining_Date"].ffill()


# =================
# 14. CHECK MISSING VALUES AFTER IMPUTATION

print("\n" + "=" * 60)
print("MISSING VALUES AFTER IMPUTATION")
print("=" * 60)

print(df.isnull().sum())

print(
    "\nTotal Missing Values:",
    df.isnull().sum().sum()
)


# ============================================================
# 15. REMOVE DUPLICATE RECORDS

print("\n" + "=" * 60)
print("REMOVING DUPLICATES")
print("=" * 60)

before_duplicates = len(df)

df = df.drop_duplicates()

after_duplicates = len(df)

duplicates_removed = (
    before_duplicates - after_duplicates
)

print(
    "Duplicate rows removed:",
    duplicates_removed
)

print(
    "Rows before removing duplicates:",
    before_duplicates
)

print(
    "Rows after removing duplicates:",
    after_duplicates
)


# ============================================================
# 16. CHECK DUPLICATES AGAIN

print("\nDuplicate rows remaining:")

print(df.duplicated().sum())


# ============================================================
# 17. CHECK EMPLOYEE ID DUPLICATES

print("\n" + "=" * 60)
print("EMPLOYEE ID CHECK")
print("=" * 60)

duplicate_employee_ids = (
    df["Employee_ID"].duplicated().sum()
)

print(
    "Duplicate Employee IDs:",
    duplicate_employee_ids
)


# ============================================================
# 18. CREATE USEFUL NEW COLUMNS
# ============================================================

# Joining year
df["Joining_Year"] = df["Joining_Date"].dt.year

# Joining month
df["Joining_Month"] = df["Joining_Date"].dt.month

# Joining month name
df["Joining_Month_Name"] = (
    df["Joining_Date"].dt.month_name()
)

# Years in company
current_year = 2026

df["Years_in_Company"] = (
    current_year -
    df["Joining_Date"].dt.year
)


# ============================================================
# 19. CREATE SALARY CATEGORY

def salary_category(salary):

    if salary < 60000:
        return "Low"

    elif salary < 100000:
        return "Medium"

    else:
        return "High"


df["Salary_Category"] = (
    df["Annual_Salary"]
    .apply(salary_category)
)


# ============================================================
# 20. CREATE PERFORMANCE CATEGORY
# ============================================================

def performance_category(score):

    if score <= 2:
        return "Needs Improvement"

    elif score == 3:
        return "Average"

    elif score == 4:
        return "Good"

    else:
        return "Excellent"


df["Performance_Category"] = (
    df["Performance_Score"]
    .apply(performance_category)
)


# ============================================================
# 21. FINAL DATASET INSPECTION

print("\n" + "=" * 60)
print("DATASET AFTER CLEANING")
print("=" * 60)

print("\nFirst 5 Rows:")
print(df.head())

print("\nFinal Shape:")
print(df.shape)

print("\nFinal Data Types:")
print(df.dtypes)

print("\nFinal Missing Values:")
print(df.isnull().sum())

print(
    "\nTotal Missing Values:",
    df.isnull().sum().sum()
)

print(
    "\nDuplicate Rows:",
    df.duplicated().sum()
)


# ============================================================
# 22. BEFORE VS AFTER COMPARISON

print("\n" + "=" * 60)
print("BEFORE VS AFTER CLEANING")
print("=" * 60)

print("\nBEFORE CLEANING")
print("----------------")
print("Rows:", 157)
print("Columns:", 12)
print(
    "Missing Values:",
    32
)
print(
    "Duplicate Rows:",
    7
)

print("\nAFTER CLEANING")
print("----------------")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print(
    "Missing Values:",
    df.isnull().sum().sum()
)
print(
    "Duplicate Rows:",
    df.duplicated().sum()
)


# 23. SOME FINAL DATA QUALITY CHECKS
# ============================================================

print("\n" + "=" * 60)
print("FINAL DATA QUALITY CHECKS")
print("=" * 60)

print(
    "\nAge Range:",
    df["Age"].min(),
    "to",
    df["Age"].max())

print(
    "\nSalary Range:",
    df["Annual_Salary"].min(),
    "to",
    df["Annual_Salary"].max()
)

print(
    "\nExperience Range:",
    df["Experience_Years"].min(),
    "to",
    df["Experience_Years"].max())

print(
    "\nPerformance Score Range:",
    df["Performance_Score"].min(),
    "to",
    df["Performance_Score"].max()
)


# 24. CLEANING SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("CLEANING SUMMARY")
print("=" * 60)

print("""
1. Loaded the messy employee dataset using Pandas.
2. Inspected the dataset structure, data types and statistics.
3. Identified and quantified missing values.
4. Removed extra spaces and standardized categorical values.
5. Converted numerical columns to appropriate numeric data types.
6. Converted Joining_Date to datetime format.
7. Used mode imputation for categorical missing values.
8. Used median imputation for numerical missing values.
9. Used forward filling for the date column.
10. Removed duplicate records using drop_duplicates().
11. Created useful date-based and employee-related columns.
12. Created salary and performance categories using apply().
13. Verified missing values and duplicate records after cleaning.
14. Exported the final cleaned dataset as a CSV file.""")



# 25. EXPORT CLEANED DATASET
# ============================================================

output_file = "Cleaned_Company_Employee_Dataset.csv"

df.to_csv(
    output_file,
    index=False
)

print("\n" + "=" * 60)
print("EXPORT COMPLETED")
print("=" * 60)

print(
    f"Cleaned dataset saved as: {output_file}"
)