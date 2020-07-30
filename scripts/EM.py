#encoding=utf8
""" 
EM算法与混合高斯分布 
author:luchi 
date:2015/12/6 
 
description：假如有一堆人，包括男的和女的，现在不知道 
其比例只能统计身高信息，现在要求男的和女的的身高的均值 
方差已经在人群中占得比例，使用EM算法的混合高斯模型可以 
解决 
"""  
from numpy import *  
from random import *  
import math  
  
#计算高斯值  
def calcGauss(x,mu,sigma):  
    return exp(-1*(x-mu)**2/2/(sigma**2))/sigma/sqrt(2*math.pi)  
      
#计算均值  
def averageHeight(height,gamma,n):  
    sumHeight=0.0  
    for i in range(len(height)):  
        sumHeight+=height[i]*gamma[i]  
    return float(sumHeight)/n  

#计算标准差  
def varianceHeight(height,gamma,mu,n):  
    sumVariance=0.0  
    for i in range(len(height)):  
        sumVariance+=gamma[i]*(height[i]-mu)**2  
    return sqrt(float(sumVariance)/n)  
  
#终止条件gp,bp,gmu,gsigma,bmu,bsigma  
def isEqual(cur,now):  
    cur=mat(cur).T  
    now=mat(now).T  
    temp=cur-now  
    if temp.T*temp<0.001:  
        return True  
    return False  
      
#计算的主要函数，height为人群的身高分布  
def calcEM(height):  
    N=len(height)  
    gp=0.5  #女孩的初始比例  
    bp=0.5  #男孩的初始比例  
    gmu,gsigma=min(height),1  #初始值的女孩身高均值和标准差  
    bmu,bsigma=max(height),1  #初始值的男孩身高均值和标准差  
      
    ggamma=list(range(N))  #计算女孩在迭代过程中的gamma值  
    bgamma=list(range(N))  #计算女孩在迭代过程中的gamma值  
      
    cur=[gp,bp,gmu,gsigma,bmu,bsigma] #初始的方差矩阵  
    now=[]  
      
    times=0  #迭代次数  
    while times<100:  
        i=0  
        for x in height:  
           ggamma[i]= gp*calcGauss(x,gmu,gsigma)  
           bgamma[i]= bp*calcGauss(x,bmu,bsigma)  
           s= ggamma[i]+bgamma[i]  
           ggamma[i]/=s  
           bgamma[i]/=s  
           i+=1  
          
        gn=sum(ggamma)  #计算比例  
        gp=float(gn)/float(N)  
        bn=sum(bgamma)  
        bp=float(bn)/float(N)  
        gmu=averageHeight(height,ggamma,gn)  
        gsigma=varianceHeight(height,ggamma,gmu,gn)  
        bmu=averageHeight(height,bgamma,bn)  
        bsigma=varianceHeight(height,bgamma,bmu,bn)  
  
        now=[gp,bp,gmu,gsigma,bmu,bsigma]  
        if isEqual(cur,now):  
            break  
        cur=now  
  
        print("迭代次数是：\t",times)
        print("女孩的身高平均值和标准差是:\t",gmu,gsigma)
        print("男孩的身高平均值和标准差是:\t",bmu,bsigma)
        print("男孩女孩的比例是：\t",bn,gn,bn+gn)
        times+=1  
    return now  
  
def test():  
    #产生随机测试集  
    height=[]  
    #产生男生的身高数据  
    for i in range(500):  
        height.append(gauss(175,2)+5*random()*pow(-1,i))  
    for i in range(900):  
        height.append(gauss(160,2)+5*random()*pow(-1,i))  
      
    calcEM(height)  
  
if __name__=='__main__':  
    test()  
      
          
  
  
  
  