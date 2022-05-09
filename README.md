# Reading-writing-csv

Open a CSV File
f = open('filename.csv')


Character	Mode	         Description
‘r’	      Read (default)	Open a file for read only
‘w’	      Write	          Open a file for write only (overwrite)
‘a’	      Append	        Open a file for write only (append)
‘r+’	    Read+Write	    open a file for both reading and writing
‘x’     	Create	        Create a new file

•	csv.reader – read data from a csv file

•	csv.writer – write data to a csv file

Python Pandas Module
Pandas is a popular data science library in Python for data manipulation and analysis. If we are working with huge chunks of data, it's better to use pandas to handle CSV files for ease and efficiency.

Once we install it, we can import Pandas
To Read a CSV:
To read the CSV file using pandas, we can use the read_csv() function

To Write to a CSV:
To write to a CSV file, we need to call the to_csv() function of a DataFrame.
