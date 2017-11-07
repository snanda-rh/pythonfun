import pandas as pd


#################################################
# Write to a csv
#################################################


newCSV = pd.read_csv('TestData.csv', header=0, names= ["Food","price","Quantity"], usecols = [1,2,3])

print newCSV


#Create a new csv edited
newCSV.to_csv('TestData2.csv')
