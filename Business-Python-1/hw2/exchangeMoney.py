def change(w, x, y, z):
    '''
    w -> 50
    x -> 10
    y -> 5
    z -> 1
    '''
    money = 50*w + 10*x + 5*y + 1*z
    return money

def main():
    w = int(input("input number of $50: "))
    x = int(input("input number of $10: "))
    y = int(input("input number of $5: "))
    z = int(input("input number of $1: "))
    money = change(w, x, y, z)
    print(money)

if __name__ == '__main__':
    main()