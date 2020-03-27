'''
報社訂報紙：今天下午下單，明天清晨收單並付款
1. 每份報紙的進貨價格： c
2. 賣給客人的零售價： r
3. 每份沒賣出去的，隔天可以以一份 s元 的殘直當廢紙賣出

每天多少客人(需求量 D)是隨機的
明天的訂單需求量會落在 0~N之間 -> Pr(D=i) = p_i, i = 1, 2, ...N

決定定貨量 q* 去最大化期望利潤
pi(q) = r * expetation[ min(q, D) ] - (c*q) + s * expectation[ max(q-D, 0)] 

其中：
1. min(q, D)是明天的銷售量(訂貨量與需求量比較小的數字)
2. expetation[ min(q, D) ] 是預期銷售量
3. r * expetation[ min(q, D) ] 是預期銷售收益
4. max(q-D, 0) 是沒賣掉的份數
5. s * expectation[ max(q-D, 0)] 是預期總殘直

'''


import numpy as np 
import sys 

def main():
    # input the data
    filename = sys.argv[1]
    with open("%s" % filename, "r") as f:    
        data = f.read()   
    data = data.split("\n")

    c = int(data[0])
    r = int(data[1])
    N = int(data[2])
    s = int(data[3])

    demand_array = np.zeros(N+1)
    for i in range(N+1):
        demand_array[i] = float(data[i+4])
    print('----- parameter -----')
    print(c, r, N, s)
    print(demand_array)
    print("\n")

    result_array = np.zeros((2, N+1))
    print('----- start calculating -----')
    for i in range(N+1):
        result_array[0, i] = i
        result_array[1, i] = cal_expectation(c, r, i, s, demand_array)

    print("\n", "----- result table -----")
    print(result_array)

def cal_expectation(c, r, q, s, demand_array):
    
    if q == 0:
        print("q = 0: ", 0)
        return 0
    else:
        sum_expectation = 0
        p_demand = 0
        for i in range(q):
            expectation = r*i - c*q + s*(q-i) 
            expectation = expectation * demand_array[i]
            sum_expectation = sum_expectation + expectation
            p_demand = p_demand + demand_array[i] 
        expectation_sellall = r*q - c*q
        expectation_sellall = expectation_sellall * (1 - p_demand)
        sum_expectation = sum_expectation + expectation_sellall
        print("q = %d: " % (i+1), sum_expectation)
        return sum_expectation

if __name__ == '__main__':
    main()















