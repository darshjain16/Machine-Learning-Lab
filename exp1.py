import pandas as pd

# Creating a Series
series = pd.Series([10, 20, 30, 40, 50], name="Numbers")
print("Series:\n", series)

# Creating a DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# Accessing columns
print("\nAccessing column 'Name':\n", df["Name"])

# Accessing rows with loc
print("\nAccessing row 0 with loc:\n", df.loc[0])

# Accessing rows with iloc
print("\nAccessing row 1 with iloc:\n", df.iloc[1])

# Accessing subsets
print("\nSubset (Name and City columns):\n", df.loc[:, ["Name", "City"]])

# Adding missing values
df.loc[3] = [None, 28, "San Francisco"]
print("\nDataFrame with missing values:\n", df)

# Filling missing values
df["Name"].fillna("Unknown", inplace=True)
print("\nAfter filling missing values:\n", df)

# Dropping rows with missing values
df.dropna(inplace=True)
print("\nAfter dropping rows with missing values:\n", df)

data = {
    "Category": ["A", "A", "B", "B", "C"],
    "Values": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Grouping and aggregating
grouped = df.groupby("Category")["Values"].sum()
print("\nGrouped and aggregated data:\n", grouped)

# Merging
data1 = {"ID": [1, 2], "Name": ["Alice", "Bob"]}
data2 = {"ID": [1, 2], "City": ["New York", "Los Angeles"]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
merged = pd.merge(df1, df2, on="ID")
print("\nMerged DataFrame:\n", merged)

# Concatenation
df3 = pd.DataFrame({"Values": [100, 200]})
concatenated = pd.concat([df, df3], axis=1)
print("\nConcatenated DataFrame:\n", concatenated)

# Filtering
filtered = df[df["Values"] > 20]
print("\nFiltered DataFrame (Values > 20):\n", filtered)

# Sorting
sorted_df = df.sort_values(by="Values", ascending=False)
print("\nSorted DataFrame:\n", sorted_df)

# Writing to CSV
df.to_csv("example.csv", index=False)

# Reading from CSV
df_csv = pd.read_csv("example.csv")
print("\nDataFrame read from CSV:\n", df_csv)

# Writing to Excel
df.to_excel("example.xlsx", index=False)

# Reading from Excel
df_excel = pd.read_excel("example.xlsx")
print("\nDataFrame read from Excel:\n", df_excel)

# Pivot table
pivot = df.pivot_table(values="Values", index="Category", aggfunc="sum")
print("\nPivot Table:\n", pivot)

# Multi-indexing
df_multi = df.set_index(["Category", "Values"])
print("\nMulti-index DataFrame:\n", df_multi)

# Reshaping with melt
reshaped = df.melt(id_vars=["Category"], var_name="Attribute", value_name="Value")
print("\nReshaped DataFrame:\n", reshaped)

