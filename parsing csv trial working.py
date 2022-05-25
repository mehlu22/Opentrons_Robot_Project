import pandas as pd
#Command to read the entire csv file
dataset = pd.read_csv('3-end_seq_scheme_051822_v1.csv', delimiter = ",", index_col = False)
print(dataset)

#Command to print out the first 5 rows of the csv file
print(dataset.head(15))
print()

#Command to print out the last 5 rows of the csv file
print(dataset.tail(10))
print()

#Command to print out the first 5 rows of the 'reagent_name' column
print(dataset['reagent_name'].head())
print()

#Command to print the type of the dataset
print(type(dataset))
print()

#Command to obtain all columns of a row in the form of an array
print(dataset.values)
print()

#Command to obtain all the columns of a row using a column of the row
dataset.set_index("reagent_name", inplace = True)
print(dataset.loc['FS1'])
print()

#Command to print specific position using row and column in the csv file
print(dataset.iloc[0,0])
print(dataset.iloc[0,1])
print(dataset.iloc[0,2])
print(dataset.iloc[1,0])
print(dataset.iloc[1,1])
print(dataset.iloc[1,2])
            

