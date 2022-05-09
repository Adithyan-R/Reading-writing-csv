import pandas as pd

# creating a data frame
df = pd.DataFrame([['Data1', 12], ['Data2', 32]], columns = ['Title', 'Id'])

# writing data frame to a CSV file
df.to_csv('data1.csv')

#reading data in csv 
rw=pd.read_csv("data1.csv")

rw
