import pandas as pd

print("Darsh jain - 1/22/FET/BCS/182")
'\n'
#loading the set 
dataframe = pd.read_excel("C:/Users/Lenovo/Desktop/ML/Student-List-Exp.xlsx")
print(dataframe)
'\n'
#rename the dataset
df = dataframe.rename(columns={"Branch/Course":"Course","University Registration No.(Issued by R&S Branch)":"Registration no.",
                        "Date of Admission in the Present Class/Course":"Admission Date","Aadhaar No. of Student":"Aadhaar No."
                        ,"Updated Mobile No. of Student":"Mobile No.","Updated E-mail ID":"E-mail ID",
                        "Spelling strictly as per Registration record in Capital Letters (Issued by R&S Branch)-SN":"Student Name",
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
print("Number of Males and females :")
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
result = df[(df['Total Due Fee Pending'].notnull()) & (df['Total Due Fee Pending'] > 0)]
print("\nStudents having pending dues:")
result = result[['Student Name','Total Due Fee Pending']]
print(result, '\n')


#extract specific columns like name. roll no. mentor 
data = df[['Student Name','Roll No.','mentors']]
print(data, '\n')

#list of students where Aadhar number is not available 
data = df[df['Aadhaar No.'].isnull()]
print("List of students where Aadhar number is not available:")
print(data['Student Name'],'\n')

#remaining the column names in the excel sheet 
df.to_excel("C:/Users/Lenovo/Desktop/ML/Student-List-Exp.xlsx",index = False)
print("Columns have been renamed and saved back to the Excel file.",'\n')