import os
import pandas as purchase_data
 
# specify your path of directory
path = r"C:\Users\julie"
 
# call listdir() method
# path is a directory of which you want to list
directories = os.listdir( path )

# create Dataframe to hold all data imported from the files. 
dataDF = pd.Dataframe(columns=['Date', 'Last Name', 'First Name', 'Middle Name', 'Email', 'Phone Number','Class', 
    'Specialty', 'Facility'])

# This would print all the files and directories
for file in directories:
   print(file)
   #open each file and load data to pandas 
   data = pd.read_excel(file)
   
   dataDF.append(data)