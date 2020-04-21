import numpy as np 

def create_wall(n):
    wall_arr = np.ones(n,)
    return wall_arr

def painting(wall, start, end, color):
    start_idx = start - 1
    end_idx = end
    wall[start_idx: end_idx] = color
    return wall

def counting(wall, color_idx):
    number = []
    for i in range(len(color_idx)):
        c = 0
        for j in wall:
            if color_idx[i] == j:
                c += 1
        number.append(c)
    return number 

def print_output(number, color_idx):
    outstr = '{} {}'.format(number[0], color_idx[0])
    for i in range(1, len(number)):
        outstr = outstr + ';'
        outstr = outstr + '{} {}'.format(number[i], color_idx[i])
    print(outstr)
        


if __name__ == '__main__':
    n = int(input("input the number of wall: "))
    m = int(input("input the iter of painting: "))
    print("-------- start painting ----------")
    wall = create_wall(n)
    color_idx = []
    for i in range(m):
        print("input start idx, end idx of wall, and the color: ")
        start = int(input("input start idx: "))
        end = int(input("input end idx: "))
        color = int(input("input color: "))
        wall = painting(wall, start, end, color)
        color_idx.append(color)
    print("color index: ", color_idx)
    print("wall: ", wall)
    number = counting(wall, color_idx)
    print_output(number, color_idx)


