Task 1: Data Cleaning and Preprocessing
Objective

Clean and prepare a raw dataset by handling missing values, removing duplicates, fixing inconsistent formats, and preparing the dataset for analysis or modeling.

Tools Used

Python (Pandas)
or

Excel

Steps Performed
1. Loaded the Dataset

Used Pandas read_csv() to import the dataset into a DataFrame.

2. Inspected the Dataset

Checked:

Data types

Missing values

Duplicate entries

Summary statistics

Using:

df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()

3. Handled Missing Values

Numerical columns filled with median.

Categorical columns filled with mode.

Dropped rows only if data was completely unusable.

4. Removed Duplicate Records

Used:

df.drop_duplicates(inplace=True)

5. Standardized Text Values

Converted text to lowercase / title case

Trimmed extra spaces

Ensured category names were consistent

Example:

df['Gender'] = df['Gender'].str.lower().str.strip()

6. Corrected Date Formats

Converted dates into a consistent format:

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

7. Cleaned and Renamed Columns

Renamed columns to be:

lowercase

snake_case

without spaces

df.columns = df.columns.str.lower().str.replace(" ", "_")

8. Corrected Data Types

Ensured numeric and datetime fields had proper types.
Deliverables

Cleaned dataset (cleaned_dataset.csv)
Short summary of changes
Python notebook with cleaning steps

Summary of Changes Made

Removed duplicate rows

Filled missing values appropriately

Standardized text fields

Fixed inconsistent date formats

Renamed columns for readability

Corrected incorrect data types

Exported structured, analysis-ready dataset
