import numpy as np 
import sys

def load_data():
    filename = sys.argv[1]
    with open("%s" % filename, "r") as f:
        data = f.read()
    # print(data)
    data = data.split()
    # print(data)
    # print(len(data))
    ## create array to save the value
    save_array = np.zeros((len(data), ))
    for i in range(len(data)):
        save_array[i] = int(data[i])
    save_array = save_array.reshape(-1, 3)
    return save_array

def cal_dist(x1, y1, x2, y2, d):
    if (x1 - x2)**2 + (y1 - y2)**2 <= d**2:
        return True
    else:
        return False

def cal_people(n, d, save_array):
    ## create list to save the result
    result = []

    for i in range(1, n+1):
        print('----- start checking point %d -----' % i)
        p_x1 = save_array[i][0]
        p_y1 = save_array[i][1]
        p_dic = {'point': i, 'near':0 , 'people':0}
        nearPoint = []
        people = 0

        for j in range(1, n+1):
            p_x2 = save_array[j][0]
            p_y2 = save_array[j][1]
            if cal_dist(p_x1, p_y1, p_x2, p_y2, d) == True:
                print('   add point %d' % j)
                nearPoint.append(j)
                people = people + save_array[j][2]

        p_dic['near'] = nearPoint
        p_dic['people'] = people
        result.append(p_dic)
    return result


# 找到人數最多的點
def find_point(arr, n):
    max_people = 0
    for i in range(n):
        if arr[i]['people'] > max_people:
            max_people = arr[i]['people']
            idx = arr[i]['point']
            near_list = arr[i]['near'] 
    return max_people, idx, near_list

def main():
    data_array = load_data()
    print(data_array)
    n = int(data_array[0][0])
    p = int(data_array[0][1])
    d = data_array[0][2]

    total_choose = []
    total_people = 0
    for i in range(p):
        print('\n', ' ----- iteration {} -----'.format(i+1))
        result_dict = cal_people(n, d, data_array)
        max_people, idx, near_list = find_point(result_dict, n)
        total_people = total_people + max_people
        print("choose point {}   {} people can receive signal".format(idx, max_people))
        total_choose.append(idx)
        data_array[idx][2] = 0
        for i in near_list:
            data_array[i][2] = 0
    print('chosen point: ', total_choose)
    print('total people can receive signal: {}'.format(total_people))


if __name__ == '__main__':
    main()

