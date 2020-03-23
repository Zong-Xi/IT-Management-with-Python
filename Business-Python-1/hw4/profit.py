'''
你經營一家報攤專賣一份日報，今天下午你得在報社關門前下訂單，
告訴報社你要為明天訂購幾份報紙，隔天清晨你就會收到訂購的報紙並且付款。

1 每份報紙的進貨價格是 c 元
2 賣給客人的零售價則是 r 元
3 每天會來多少個客人想買報紙是件不確定的事，也就是說單日需求量 D 是隨機的
4 根據過往經驗，你估計明天的單日需求量會落在 0 和 NN 之間，並且符合如下的機率分佈：
        P(D = i) = p_i, i = 0, 1, 2, ...N

意思是，有 0 個人來買報紙的機率是 p_0, 有 1 個人來買報紙的機率是 p_1
最後是賣出 N 份報紙的機率是 p_N

想要決定定貨量 q* 去最大化利潤：
    pi(q) = gamma * ( E[ min {q, D}] ) - CQ
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
    save_array = np.zeros(N)
    for i in range(N):
        save_array[i] = cal_expectation(c, r, q, p_array)
        print(save_array[i])
    output = int(max(save_array))
    print("max expectation: ", output)

if __name__ == '__main__':
    c = int(input("input the cost: "))
    r = int(input("input the price: "))
    N = int(input("input the number of demand: "))
    q = int(input("input the number of order: "))
    p_array = np.zeros(N + 1)
    for i in range(N + 1):
        p_array[i] = p_array[i] + float(input("input the p_i: "))
    print(p_array)
    main()


