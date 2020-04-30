import csv

stockfn = "stock_data.txt"
fh1 = open(stockfn, 'r', encoding='cp950', newline='')
'''
readline()只會依次讀取一行，傳入變數
因此若是:
f1 = fh1.readline()
f2 = fh1.readline()
f3 = fh3.readline()

則 print(f1, f2, f3)
會分別輸出文件的第 1 2 3 行
'''

cheader = fh1.readline()
reader1 = csv.reader(fh1, delimiter='\t')


print(cheader)
for i in range(10):
    print(next(reader1))

