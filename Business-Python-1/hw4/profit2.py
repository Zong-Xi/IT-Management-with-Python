'''
求 p* 與 pi
'''
import numpy as np

def cal_expectation(c, r, q, p_array):
    expectation = 0   ## total expectation
    p = 0             ## total p for not sale out

    if q == 0:
        return 0
    else: 
        for i in range(q):
            ## not sale out
            profit_i = -(c * q) + (r * i)
            exp_profit_i = p_array[i] * profit_i
            p = p + p_array[i]
            expectation = expectation + exp_profit_i
        
        ## sale out
        profit_j = -(c * q) + (r * q)
        exp_profit_j = (1 - p) * profit_j
        print(exp_profit_j)
        expectation = expectation + exp_profit_j

        return expectation

def main():
    save_array = np.zeros(N)    ## save i-th expectation
    result_array = np.zeros([2, N])  ## save all expectation
    for i in range(N):
        save_array = np.zeros(N)
        for j in range(N):
            save_array[j] = cal_expectation(c, r, i, p_array)
        output_exp = int(max(save_array))
        result_array[0, i] = i
        result_array[1, i] = output_exp 
    print(result_array)
    result_exp = int(max(result_array[1, :]))
    print("max expectation: ", result_exp)

if __name__ == '__main__':
    c = int(input("input the cost: "))
    r = int(input("input the price: "))
    N = int(input("input the number of demand: "))
    p_array = np.zeros(N + 1)
    for i in range(N + 1):
        p_array[i] = p_array[i] + float(input("input the p_i: "))
    print(p_array)

    main()