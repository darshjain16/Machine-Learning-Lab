import pandas as pd
#loading the set 
df = pd.read_excel("C:/Users/Lenovo/Desktop/ML/Student-List-Exp.xlsx")
print(df)
'\n'
#rename the dataset
df = df.rename(columns={"Branch/Course":"Course","University Registration No.(Issued by R&S Branch)":"Registration no.",
                        "Date of Admission in the Present Class/Course":"Admission Date","Aadhaar No. of Student":"Aadhaar No."
                        ,"Updated Mobile No. of Student":"Mobile No.","Updated E-mail ID":"E-mail ID",
                        "Fee Paid for Current Semester / (Previous semester if pending)":"Fee Paid Pending",
                        "Total Due Fee for Current Semester / (Previous semester if pending)":"Total Due Fee Pending"})
print(df)
# count the total no. of rows and parameters
'\n'
rows, columns = df.shape
print(f"Total no of rows : {rows}")
print(f"Total no of parameters : {columns}")
'\n'
# count the males and females
gender_cnt = df["Gender"].value_counts()
print("Number of Male and female:")
print(gender_cnt, '\n')

#state wise count
state_cnt = df["State"].value_counts()
print("State wise count of students:")
print(state_cnt, '\n')

# Category wise count
category_cnt = df["Category"].value_counts()
print("Category wise count of students:")
print(category_cnt, '\n')

#count null values with respect to each column
null_values_cnt = df.isnull().sum()
print("Null values count in dataset:")
print(null_values_cnt, '\n')

# total count of pending dues 
pending_dues = df["Total Due Fee Pending"].value_counts()
print("Total count of dues pending:")
print(pending_dues, '\n')

#list of students with pending dues along with amount due
students_with_pending_dues = df[df['Total Due Fee Pending'].notnull()]
print("\nStudents having pending dues:")
print(students_with_pending_dues[['Student Name', 'Registration no.', 'Total Due Fee Pending']])
print("\nNo 'Fee Due' column found.")


#extract specific columns like name. roll no. mentor 
df2 = df[['Student Name','Roll No.','mentors']]
print(df2, '\n')

#list of students where Aadhar number is not available 
if df['Aadhar No.'].isnull().any():
    print("List of students where Aadhar number is not available:")
    df3 = df[df['Aadhar No.'].isnull()]['Student Name']
    print(df3, '\n')

#remaining the column names in the excel sheet 
df.to_excel("C:/Users/Lenovo/Desktop/ML/Student-List-Exp.xlsx", index = False)
print("Columns have been renamed and saved back to the Excel file.",'\n')