import sys, os
import statistics

def main():
    rr=[0,2,1,1,1,1]
    rq=[8,7,6,5,4,3,2,1,0,0,0,0,0,0]
    r=[3,1,2]
    print (meanAbsDiff(r)==myMeanAbsDiffY(r,4))
    print (avgAbsDev(r)==myAvgAbsDevY(r,4))

def avgAbsDev(r):
    n=len(r)
    avg = statistics.mean(r)
    ad=0
    for i in range(n):
        ad = ad + abs(r[i] - avg)
    return ad

def myAvgAbsDevY(r,m):
    n=len(r)
    ad=0
    avg= 0
    for i in range(2,m-1+1):
        avg = avg + (m-i)
    avg = avg/n
    for i in range(2,m-1+1):
        ad = ad + abs((m-i)- avg)
    ad = ad + (n-m+2)*(avg)
    return ad

def meanAbsDiff(r):
    n=len(r)
    mad=0
    for i in range(n):
        for j in range(n):
            mad = mad + abs(r[i] - r[j])
    return mad

def myMeanAbsDiffY(r,m):
    n=len(r)
    sum = 0
    for j in range(m-3+1):
        for i in range(m-3-j+1):
            sum = sum + i
        sum = sum + (m-2-j)*(n-m+2)
        for i in range(j+1):
            sum = sum + i
    temp=0
    for j in range(m-2+1):
        temp = temp + j
    sum = sum + (temp * (n-m+2) )
    return sum


if __name__ == "__main__":
    main()
    