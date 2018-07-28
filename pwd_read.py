import csv
def password(i,j):
    data=open(r'C:\Users\16033\Desktop\lizhengtest\project\pwd.csv','r')
    csvreader=csv.reader(data)
    data1=list(csvreader)
    data.close()
    return data1[i][j]


