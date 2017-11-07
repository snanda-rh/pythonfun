import pandas as pd


#################################################
# Introducing Data Frame- rows and columns
#################################################

data = {
'AStudents':['AJ','Mark', 'Rob','Rachel', 'Steven'],
'Maths':[98,23,43,21,52],
'Science':[32,43,32,12,32],
'Sports':['Basketball','swimming','tt','badminton','yoga']} #dictionary

# Data Frame would use the exact column names as mentioneds in the dictionary
students= pd.DataFrame(data,columns=["AStudents","Maths", "Science","Sports"])
print students



#################################################
# Reading a csv file via pandas
#################################################

#Treat the first row as header
print pd.read_csv('TestData.csv')

#In case we dont want a header
print pd.read_csv('TestData.csv', header = None)
#Rename the headers
print pd.read_csv('TestData.csv', names = ['pizza','hamburger','chocolate','shakes'])

# Treat header as row 0
print pd.read_csv('TestData.csv', names = ['pizza','hamburger','chocolate','shakes'],header=0)

# Treat header as row 1
print pd.read_csv('TestData.csv', names = ['pizza','hamburger','chocolate','shakes'],header=1)

#################################################
# Use only specific columns from the csv
#################################################


print pd.read_csv('TestData.csv', usecols=[0,1])

print pd.read_csv('TestData.csv', usecols=[0,1,2])


##################################################
