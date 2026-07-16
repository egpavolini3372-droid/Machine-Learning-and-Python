import csv
from typing import Iterable

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        header = next(reader)
        data =[]
        for row in reader:
            iterable = zip(header, row) 
           
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data
      
if __name__ == "__main__":
     data = read_csv( r"C:\Users\erwan\OneDrive\Desktop\SINTAXIS INDENTATION\Python Functions and Errors\App\data.csv")
     print(data[0])
    
    