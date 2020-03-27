def change(a):
    '''
    消費金額: a (0 <= a <= 1000)
    找錢規則: 與其給5張100，不如給1張500；與其給2個50，不如給1張100...
    錢幣: 500 -> 100 -> 50 -> 10 -> 5 -> 1
    '''
    total = 1000 - a
    p = q = r = x = y = z = 0
    if total >= 500:
        p = int(total / 500)
        total = total - p*500
    if total >= 100:
        q = int(total / 100)
        total = total - q*100
    if total >= 50:
        r = int(total / 50)
        total = total - r*50
    if total >= 10:
        x = int(total / 10)
        total = total - x*10
    if total >= 5:
        y = int(total / 5)
        total = total - y*5
    if total >= 1 :
        z = total
    return p, q, r, x, y, z

def printout(p, q, r, x, y, z):
    output = ''
    if p != 0:
        output = output + "500, " + str(p) 
    if q != 0:
        output = output + "; 100, " + str(q)
    if r != 0:
        output = output + "; 50, " + str(r)
    if x != 0:
        output = output + "; 10, " + str(x)
    if y != 0:
        output = output + "; 5, " + str(y)
    if z != 0:
        output = output + "; 1, " + str(z)
    if p == 0:
        output = output[2:]
    return output 

def main():
    a = int(input("money of the item: "))
    p, q, r, x, y, z = change(a)
    print(printout(p, q, r, x, y, z))


if __name__ == '__main__':
    main()