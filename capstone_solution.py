"""
PART 1 - A
"""

"""
1 - IMPORT EMPLOYEE FILE ONLY THE GENDER, SALARY GRADE AND DEPT COLUMNS
"""
"""
********** SETUP CODE *************
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df = pd.read_csv("emp_file_CAPSTONE.TXT")
"""
********** SETUP CODE *************
"""

# # Reads TXT file
# print(f"Prints Head and Tail: ", df)
# desired_cols = ["gender", "salary", "dept"]
# df_selected = df[desired_cols]

# print(df_selected)

# """
# 2 - FIX THE COLUMN DEPT (CAPITALIZE) IT.
# """

# df_selected = df[["gender", "sg", "dept"]].rename(columns={"dept": "Dept"})

# print(df_selected)

# """
# 3 - CREATE A DATA FRAME FOR EVERY SALARY GRADE WITH RATIO OF MEN TO WOMEN.
# """

# grouped = df.groupby(["sg", "gender"])["fn"].count().unstack()

# for sg in grouped.index:
#     # get the male and female counts for the salary grade
#     male_count = grouped.loc[sg, "M"] if "M" in grouped.columns else 0
#     female_count = grouped.loc[sg, "F"] if "F" in grouped.columns else 0

#     df_salary_group = pd.DataFrame(
#         {"Male": male_count, "Female": female_count}, index=[sg]
#     )

#     print(f"Salary Grade {sg}:\n{df_salary_group}\n")

# """
# 4 - CREATE PIE CHARTS FOR EVERY SALARY GRADE WITH THE RATIO OF MEN TO WOMEN.
# """

# import matplotlib.pyplot as plt

# grouped = df.groupby(["sg", "gender"])["fn"].count().unstack()

# # create a pie chart for each salary grade
# for sg in grouped.index:
#     # get the male and female counts for the salary grade
#     male_count = grouped.loc[sg, "M"] if "M" in grouped.columns else 0
#     female_count = grouped.loc[sg, "F"] if "F" in grouped.columns else 0

#     # create a pie chart for the salary grade
#     labels = ["Male", "Female"]
#     sizes = [male_count, female_count]
#     plt.pie(sizes, labels=labels, autopct="%1.1f%%")
#     plt.title(f"Salary Grade {sg} - Male/Female Ratio")
#     plt.show()

# """
# 5 - CREATE A DATA FRAME FOR EVERY DEPT (INDEX) WITH COLUMNS 'MALE' AND 'FEMALE'.
# """

# grouped = df.groupby(["dept", "gender"])["fn"].count().unstack()
# dept_dfs = {}
# for dept in grouped.index:
#     male_count = grouped.loc[dept, "M"] if "M" in grouped.columns else 0
#     female_count = grouped.loc[dept, "F"] if "F" in grouped.columns else 0

#     df_dept = pd.DataFrame({"Male": male_count, "Female": female_count}, index=[dept])

#     dept_dfs[dept] = df_dept

# for dept, df_dept in dept_dfs.items():
#     print(f"Department Group: {dept}\n{df_dept}\n")

# """
# 6 - CREATE A PIE CHARTS FOR EVERY DEPT WITH THE RATION OF MEN TO WOMEN.
# """

# grouped = df.groupby(["dept", "gender"])["fn"].count().unstack()

# # create a pie chart for each department
# for dept in grouped.index:
#     # get the male and female counts for the department
#     male_count = grouped.loc[dept, "M"] if "M" in grouped.columns else 0
#     female_count = grouped.loc[dept, "F"] if "F" in grouped.columns else 0

#     # create a pie chart for the department
#     labels = ["Male", "Female"]
#     sizes = [male_count, female_count]
#     plt.pie(sizes, labels=labels, autopct="%1.1f%%")
#     plt.title(f"{dept} - Male/Female Ratio")
#     plt.show()

"""
PART 1 - B
"""

"""
1 - IMPORT EMPLOYEE FILE ALL COLUMNS
"""
# df = pd.read_csv("emp_file_CAPSTONE.TXT")
# print(df)

"""
2 - FIX THE CASE ON THE LAST NAME
"""
# convert last names to title case
# we using the str.title() method to convert the last names in the 'ln' column to title case, which capitalizes the first letter of each word and converts the rest of the letters to lowercase.
# df['ln'] = df['ln'].str.title()

# print(df)
"""
3 - CREATE A FIELD CALL NAME WHICH HAS THE LASTNAME, FIRSTNAME, AND MIDDLE.
"""
# create a new 'Name' field
# df['ln'] = df['ln'].str.title()
# df['Name'] = df['ln'] + ', ' + df['fn'] + np.where(df['mi'].isna(), '', ' ' + df['mi'])

# display the modified data frame
# print(df)

# Use the np.where() function to conditionally add the middle initial to the string only if it is not null or NaN.

# The np.where() function takes three arguments: a boolean condition, a value to use if the condition is True, and a value to use if the condition is False. In this case, the use df['mi'].isna() as the condition, which returns a boolean series indicating whether each value in the 'mi' column is null or NaN. You use an empty string '' as the value to use if the condition is TRUE, which effectively removes the middle initial from the string. You use ' ' + df['mi'] as the value to use if the condition is False, which adds a space and the middle initial to the string.

"""
4 - CREATE A ALPHABETIC LIST OF EMPLOYEES BY LAST NAME, FIRST NAME.
"""

# df["ln"] = df["ln"].str.title()
# # account for upper case and lower case data
# df["dept"] = df["dept"].str.lower()
# # accounts for NaN middle initial which throws no name if no middle initial
# df["Name"] = df["ln"] + ", " + df["fn"] + np.where(df["mi"].isna(), "", " " + df["mi"])

# # sorts the data frame by last name and first name
# df_sorted = df.sort_values(by=["ln", "fn"])

# # selects the 'Name' column
# df_list = df_sorted[["Name"]]

# # display the list of employees names in alpha
# print(df_list)

"""
5 - CREATE A ALPHABETIC LIST OF EMPLOYEES BY LAST NAME, FIRST NAME, FOR EACH DEPT.
"""

# # create a new 'Name' field
# # adjust for all caps name
# df["ln"] = df["ln"].str.title()
# # account for upper case and lower case data
# df["dept"] = df["dept"].str.lower()
# # accounts for NaN middle initial which throws no name if no middle initial
# df["Name"] = df["ln"] + ", " + df["fn"] + np.where(df["mi"].isna(), "", " " + df["mi"])

# # sort_values - sorts the data frame in ascending order by department first, by lastname, and firstname
# df_sorted = df.sort_values(by=["dept", "ln", "fn"])

# # creates new data frame
# df_list = df_sorted[["Name", "dept"]]

# # this groups the data frame by the 'dept' column and creates a group for each unique department value.
# grouped = df_list.groupby("dept")

# # display the list of employees by department
# for dept, data in grouped:
#     print(f"\n{dept}")
#     print(data)

"""
6 - CREATE A HORIZONTAL BAR CHART WITH THE NUMBER OF EMPLOYEES PER DEPT.
"""

# df["dept"] = df["dept"].str.lower()
# df_sorted = df.sort_values(by=["dept"])
# df_list = df_sorted[["dept"]]
# grouped = df_list.groupby("dept").size()
# plt.barh(grouped.index, grouped)

# plt.xlabel('Number of Employees')
# plt.ylabel('Department')
# plt.title('Number of Employees Per Department')

# # display the chart
# plt.show()

"""
PART 2 - A
1 - REMOVE THE NaN from mi.
"""

# df["ln"] = df["ln"].str.title()
# df["dept"] = df["dept"].str.lower()
# df["Name"] = df["ln"] + ", " + df["fn"] + np.where(df["mi"].isna(), "", " " + df["mi"])

# df_sorted = df.sort_values(by=["ln", "fn"])

# df_list = df_sorted[["Name"]]

# print(df_list)

# used in previous code this concatenate fn + ln and add the initial or an empty string is NaN
"""
2 - Import the dept_Capstone.txt file.
"""
# import pandas as pd

# df = pd.read_csv("dept_CAPSTONE.txt")
# print(df.columns)
# print(df)

"""
3 - MAKE THE DEPT CODE ALL CAPS
"""

# QUOTES WERE NEEDED WHICH MAKES IT A STRING LITERAL INSTEAD OF A COLUMN NAME
# df["'deptCode'"] = df["'deptCode'"].str.upper()

# print(df)

"""
4 - REMOVE THE NON ALPHA CHARACTERS IN TEH DEPT NAME.
"""


# df["'dept name'"] = df["'dept name'"].str.replace(r'[^a-zA-Z\s]+', '')


# print(df)

"""
5 - Make the dept name each word initial caps.
"""

# capitalize first letter of each word in dept name
# df["'dept name'"] = df["'dept name'"].str.title()

# # display the updated data frame
# print(df)

"""
6 - COMBINE THE EMP_FILE AND THE DEPT_FILE AND JOIN BOTH TABLES ON DEPT CODE.
"""

# emp_df = pd.read_csv("emp_file_CAPSTONE.txt")

# dept_df = pd.read_csv("dept_CAPSTONE.txt")

# # REPLACE QUOTES WITH NO QUOTES
# dept_df.columns = dept_df.columns.str.replace("'", "")

# # RENAME COLUMNS
# dept_df = dept_df.rename(columns={"deptCode": "DeptCode", "dept name": "DeptName"})

# dept_df["DeptCode"] = dept_df["DeptCode"].str.replace("'", "")

# dept_df["DeptName"] = dept_df["DeptName"].str.replace("'", "")

# # print(dept_df)

# merged_df = pd.merge(emp_df, dept_df, left_on='dept', right_on="DeptCode")

# print(merged_df)

'''
7 - CREATE A FILE CALLED ACTIVE_EMPLOYEES_BY_DEPT. PRINT LIST OF ALL EMPLOYEES BY DEPT BY HIRE DATE (DESCENDING ORDER) WITH TERMINATED EMPLOYEES ELIMINATED.
'''


# UNSURE OF ANSWER


'''
8 - CREATE A HISTOGRAM THAT SHOWS A COUNT OF THE NUMBER OF EMPLOYEES PER DEPT BY YEARS EMPLOYED.
'''
# import pandas as pd
# from datetime import datetime

# # read in the data from a csv file
# df = pd.read_csv('emp_file_CAPSTONE.txt')

# # convert hiredate string to datetime object
# df['hiredate'] = pd.to_datetime(df['hiredate'])

# # calculate years employed
# now = datetime.now()
# df['years_employed'] = (now - df['hiredate']).dt.days / 365

# # create a histogram of number of employees per department by years employed
# df.hist(column='years_employed', by='dept', bins=range(0, 31, 5))

# plt.show()


'''
PART 2B SALARY ANALYSIS
'''

'''
1 - DECODE THE SALARIES COLUMN
'''

# import re

# df = pd.read_csv('emp_file_CAPSTONE.txt')

# df['salary'] = df['salary'].apply(lambda x: re.sub(r'\D', '', x))

# df['salary'] = df['salary'].astype(int)

# cleaned_salaries = df['salary']

# scale = {
#     0: 7,
#     1: 8,
#     2: 9,
#     3: 0,
#     4: 1,
#     5: 2,
#     6: 3,
#     7: 4,
#     8: 5,
#     9: 6
# }

# def decode_salary(salary, scale):
#     salary_str = str(salary)
    
#     # Decode each digit using the scale
#     decoded_digits = [str(scale[int(digit)]) for digit in salary_str]
    
#     # Combine the decoded digits and convert back to an integer
#     decoded_salary = int(''.join(decoded_digits))
    
#     return decoded_salary

# # Apply the decoding function to the salary column
# df['salary'] = df['salary'].apply(decode_salary, scale=scale)

# print(df['salary'])

# '''
# 2 - CREATE A HISTOGRAM OF ALL SALARIES IN DECILES.
# '''

# df['decile'] = pd.qcut(df['salary'], q=10, labels=False)

# # Create a histogram of the binned salaries
# df.hist(column='salary', by='decile', bins=30, layout=(2, 5), figsize=(15, 6))

# # plt.show()

# '''
# CALCULATE MEAN, MODE, MEDIAN, AND STANDARD DEVIATION OF THE SALARIES.
# '''

# mean_salary = df['salary'].mean()
# print(f"Mean Calc: ", mean_salary)
# mode_salary = df['salary'].mode()[0]
# print(f"Mode Calc: ", mode_salary)
# median_salary = df['salary'].median()
# print(f'Median Calc: ', median_salary)
# std_salary = df['salary'].std()
# print(f"Standard Dev Calc: ", std_salary)

'''
5 - CALCULATE, THE MEAN, MODE, MEDIAN, AND STANDARD DEVIATION OF THE SALARIES OF MEN.
'''

# import pandas as pd

# def filter_male_salaries(df):
#     return df[df['gender'] == 'M']['salary']
#     return male_salaries

# df = pd.read_csv('emp_file_CAPSTONE.txt')
# male_salaries = filter_male_salaries(df)
# print(male_salaries)

# def filter_female_salaries(df):
#     return df[df['gender'] == 'F']['salary']

# df = pd.read_csv('emp_file_CAPSTONE.txt')
# female_salaries = filter_female_salaries(df)
# print(female_salaries)

'''
6 - CALCULATE, THE MEAN, MODE, MEDIAN, AND STANDARD DEVIATION OF THE SALARIES OF WOMAN.
'''