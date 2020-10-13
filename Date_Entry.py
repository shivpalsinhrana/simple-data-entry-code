import csv
import os.path
from os import path

Headers = [['CustomerName', 'Age', 'Location','MoneySpent']] # edit the headers here
list_data = []
a = ''
pin = '0000' # pin to cancel entry at any point

while True:
    csv_list=[]
    a = input('1. Give Custom name: ') # prompt user for first item in the list Headers 
    if a == pin:
        break
    b = input('2. Customer age: ')
    if b == pin:
        break
    c = input('3. Customer location: ')
    if c == pin:
        break
    d = input('4. Money spent by customer: ')
    if d == pin:
        break
    csv_list.append(a)
    csv_list.append(b)
    csv_list.append(c)
    csv_list.append(d)
    list_data.append(csv_list)
    x = input('Would you like to continue? (y/n): ')
    if x == 'n':
        break
    

filename = input('Give file name: ') # prompt user to give a file name or pin to cancel the entry
file1 = filename + '.csv'
file_csv= file1

if filename == pin:
    print ('Entry cancelled!')

else:
    if path.exists(file_csv)==True:                 # if the file is already created, it will update it
        with open (file1, 'a', newline='') as fp:
            a = csv.writer(fp)
            data = list_data
            a.writerows(data)
            print('File successfully updated!')
        
    else:
        with open (file1, 'a', newline='') as fp:  # if the file doesnot exist, it will create new csv file
            a = csv.writer(fp)
            file_csv = file1
            data = Headers + list_data
            a.writerows(data)
            print('File successfully created!')



