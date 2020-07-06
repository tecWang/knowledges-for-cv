import pandas as pd
import numpy as np
from numpy import random
import math
import matplotlib.pyplot as plt

'''
输入层：假设一个输入样本为X=[x1,x2,x3,…,xn]，是一个n维向量，则输入层神经元个数为n个。
    当前输入样本的维度为2， 则神经元个数为2？不对。当前样本维度为2，但是最后分了三类，
    且权重矩阵为(2, 2, 2)。个人认为应该是4个神经元

输出层（竞争层）：通常输出层的神经元以矩阵方式排列在二维空间中，每个神经元都有一个权值向量。
假设输出层有m个神经元，则有m个权值向量，Wi = [wi1,wi2,....,win], 1<=i<=m。


1. 初始化:权值使用较小的随机值进行初始化，并对输入向量和权值做归一化处理 
          X’ = X/||X|| 
          ω’i= ωi/||ωi||， 1<=i<=m 
          ||X||和||ωi||分别为输入的样本向量和权值向量的欧几里得范数。

2.将样本输入网络:样本与权值向量做点积，点积值最大的输出神经元赢得竞争，
（或者计算样本与权值向量的欧几里得距离，距离最小的神经元赢得竞争）记为获胜神经元。
3.更新权值:对获胜的神经元拓扑邻域内的神经元进行更新,并对学习后的权值重新归一化。 
        ω(t+1)= ω(t)+ η(t，n) * (x-ω(t))
        η(t，n):η为学习率是关于训练时间t和与获胜神经元的拓扑距离n的函数。
        η(t，n)=η(t)e^(-n)
        η(t)一般取迭代次数的倒数

4.更新学习速率η及拓扑邻域N,N随时间增大距离变小。
5.判断是否收敛。如果学习率η<=ηmin或达到预设的迭代次数，结束算法。
'''

#初始化输入层与竞争层神经元的连接权值矩阵
def initCompetition(n , m , d):
    #随机产生0-1之间的数作为权值
    array = random.random(size=n * m *d)
    som_weight = array.reshape(n,m,d)
    return som_weight

#计算向量的二范数
def cal2NF(X):
    res = 0
    for x in X:
        res += x*x
    return res ** 0.5

#对数据集进行归一化处理
def normalize(dataSet):
    old_dataSet = dataSet.copy()
    for data in dataSet:
        two_NF = cal2NF(data)
        for i in range(len(data)):
            data[i] = data[i] / two_NF
    return dataSet , old_dataSet

#对权值矩阵进行归一化处理
def normalize_weight(som_weight):
    for x in som_weight:
        for data in x:
            two_NF = cal2NF(data)
            for i in range(len(data)):
                data[i] = data[i] / two_NF
    return som_weight

#得到获胜神经元的索引值
def getWinner(data , som_weight):
    # print(som_weight.shape)
    # 输入数据为单个样本(1, 2), 权重矩阵为(2, 2, 2)
    max_sim = 0
    n,m,d = som_weight.shape
    mark_n = 0
    mark_m = 0
    for i in range(n):
        for j in range(m):
            if sum(data * som_weight[i,j]) > max_sim:
                max_sim = sum(data * som_weight[i,j])
                mark_n = i
                mark_m = j
    return mark_n , mark_m  # 

#得到神经元的N邻域
def getNeibor(n , m , N_neibor , som_weight):
    res = []
    nn,mm , _ = som_weight.shape
    for i in range(nn):
        for j in range(mm):
            N = int(((i-n)**2+(j-m)**2)**0.5)
            if N<=N_neibor:
                res.append((i,j,N))
    return res

#学习率函数
def eta(t,N):
    return (0.3/(t+1))* (math.e ** -N)

#SOM算法的实现
def do_som(dataSet, som_weight, T , N_neibor):
    '''
    T:最大迭代次数
    N_neibor:初始近邻数
    '''
    for t in range(T-1):
        som_weight = normalize_weight(som_weight)
        for data in dataSet:
            n , m = getWinner(data, som_weight)
            neibor = getNeibor(n, m, N_neibor, som_weight)
            for x in neibor:
                j_n=x[0];j_m=x[1];N=x[2]
                #权值调整
                som_weight[j_n][j_m] = som_weight[j_n][j_m] + eta(t,N)*(data - som_weight[j_n][j_m])
            N_neibor = N_neibor+1-(t+1)/200

    res = {}
    N , M , _ =som_weight.shape
    for i in range(len(dataSet)):
        n, m = getWinner(dataSet[i], som_weight)
        key = n*M + m
        if key in res:
        # if res.has_key(key):
            res[key].append(i)
        else:
            res[key] = []
            res[key].append(i)
    return res

def draw(C , dataSet):
    # color = ['r', 'y', 'g', 'b', 'c', 'k', 'm' , 'd']
    plt.figure()
    count = 0
    for i in C.keys():
        X = []
        Y = []
        # 变量 c 内部存储了该分类的样本索引，用于绘图时进行标记
        datas = C[i]
        for j in range(len(datas)): # 分别将每个样本的第0个属性和第1个属性加载入坐标内
            X.append(dataSet[datas[j]][0])
            Y.append(dataSet[datas[j]][1])
        plt.scatter(X, Y, marker='o', label=i)
        # plt.scatter(X, Y, marker='o', color=color[count % len(color)], label=i)
        count += 1
    plt.legend(loc='upper right')
    plt.show()

def draw_density(C_res):
    plt.figure()
    keys = list(C_res.keys())
    block = np.zeros((50, 50))
    vmax = 0
    for key in keys:
        print(len(C_res[key]))
        if len(C_res[key]) >= vmax:
            vmax = len(C_res[key])
        temp_block = np.ones((50, 50))*len(C_res[key])*10
        block = np.hstack((block, temp_block))
    # block = block[:, 50:]
    block = np.vstack((block[:, :100], block[:, 100:]))
    print(block.shape)
    print(vmax)
    plt.imshow(block, vmin=0, vmax=vmax*10+20, cmap="gray")
    plt.axis("off")

#SOM算法主方法
def SOM(dataSet, som_n, som_m, T, N_neibor):
    # som_n=2, som_m=2 为权重矩阵的宽高
    dataSet, old_dataSet = normalize(dataSet)
    som_weight = initCompetition(som_n, som_m, (dataSet)[1].shape[0])
    C_res = do_som(dataSet, som_weight, T, N_neibor)

    # print(C_res)
    draw_density(C_res)
    draw(C_res, dataSet)
    draw(C_res, old_dataSet)

dataSet = pd.read_csv("dataSet.txt", header=None)
print(dataSet.head())
SOM(dataSet.values, som_n=2, som_m=2, T=4, N_neibor=2)