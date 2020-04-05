#created by Niraj G.
#This file makes uploading and reading a csv file a lot easier especially when dealing with large amounts of data
#By default, the encoding used is utf-8-sig (in case you are wondering that is check out
#https://www.fileformat.info/info/unicode/utf8.htm)

#standard/inbuilt library for Python
import csv

#read_file looks through the file and goes line by line (think how a printer prints one line at a time on a piece of paper)
#Returned is an array (formatted as: [[row], column]) where each array value is an array representing the row. Each value of this subarray
#is the column value of that specific row
def read_file(filename, encoding='utf-8-sig'):
    with open(filename, 'r', encoding=encoding) as file:
        read = csv.reader(file, delimiter=',')
        reads =[]
        for r in read:
            reads+=[r]
        return reads

 #
def get_col(filename, column, encoding = 'utf-8-sig'):
    full = read_file(filename, encoding)
    col_data = []
    if type(column) is int:
        for f in full:
            col_data+=[f[column]]
        return col_data
    for f in full:
        col_data+=[[f[i] for i in range(0, len(f)) if i in column]]
    return col_data


def write_filedict(headers,  dataset, filename='default.csv', encoding='utf-8-sig'):
    with open(filename, 'w', encoding=encoding, newline=' ') as file:
        write = csv.Dictwriter(file, headers)
        write.writeheader()
        for d in dataset:
            if len(d)>0:
                write.writerow(d)
    return "Sucess"

def write_file(dataset, filename='default.csv', encoding='utf-8-sig'):
    try:
        with open(filename, 'w', encoding=encoding, newline='') as file:
            write = csv.writer(file, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
            for data in dataset:
                write.writerow(data)
        return 'Sucess'
    except Exception as e:
        return "ERROR returned: "+str(e)

def append(row, filename, encoding='utf-8-sig'):
    with open(filename, 'a', encoding=encoding, newline='') as file:
        append = csv.writer(file)
        append.writerow(row)
    return 'Sucess'
