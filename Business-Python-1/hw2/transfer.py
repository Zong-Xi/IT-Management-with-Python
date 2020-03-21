'''
假設我們現在有兩個帳戶，戶頭金額各為 x1 和 x2
現在想從第一個戶頭轉 y 元到第二個戶頭，一般是:
    x1 - y and x2 + y

如果第一個戶頭的錢不夠，則:
    x1 -> 0 and x2 -> x2 + x1

寫一個程式，讀入 x1, x2, y, 判斷兩戶頭應該變多少錢
'''

def transfer(x1, x2, y):
    if x1 >= y:
        x1 = x1 - y
        x2 = x2 + y
        return x1, x2
    else :
        x2 = x2 + x1 
        x1 = 0
        return x1, x2

def main():
    x1 = int(input("input the money of the first user: "))
    x2 = int(input("input the money of the second user: "))
    y = int(input("input the money you want to transfer: "))
    output1, output2 = transfer(x1, x2, y)
    print(output1, output2)

if __name__ == '__main__':
    main()