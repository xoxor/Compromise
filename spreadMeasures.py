import sys, os, statistics, math

def main():
    rr=[0,2,1,1,1,1]
    rq=[8,7,6,5,4,3,2,1,0,0,0,0,0,0]
    r=[3,2,1,0,0,0]
#   print (meanAbsDiff(r)==myMeanAbsDiffY(r,4))
#   print (avgAbsDev(rq)==avgAbsDevComputation(rq))
#   print (math.sqrt(sumStDev(rq)/len(rq)))
    print (sumStDev(rq))
    print (mySumStDev(rq))
    print (stComput(rq))

def getMofY(rY):
    return rY[0]+2

def sumStDev(r):
    n = len(r)
    avg = statistics.mean(r)
    sd = 0
    for i in range(n):
        sd = sd + math.pow(r[i] - avg,2)
    return sd

def mySumStDev(r):
    n = len(r)
    m = getMofY(r)
    avg = statistics.mean(r)
    sd = 0
    for i in range(1,m-2+1):
        sd = sd + math.pow(i,2)
    for i in range(1,m-2+1):
        sd = sd - 2*avg*i
    sd = sd + (m-2)*(math.pow(avg,2))
    sd = sd + (n-m+2)*(math.pow(avg,2))
    return sd

def stComput(r):
    n = len(r)
    m = getMofY(r)
    avg = statistics.mean(r)
    sd = (m-2)*(m-1)*(2*m-3)/6 - avg*(m-2)*(m-1)+ avg**2*(m-2)+(n-m+2)*avg**2
    sd = (m-2)*(m-1)*(2*m-3)/6 - (m-2)**2*(m-1)**2/(4*n)
    return sd

def avgAbsDev(r):
    n = len(r)
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

def avgAbsDevComputation(r):
    n = len(r)
    m = getMofY(r)
    ad = 0
    avg = statistics.mean(r)
    floor = math.floor(avg)
    for i in range(floor+1,m-2+1):
        ad = ad + (i-avg)
    for i in range(1,floor+1):
        ad = ad - (i-avg)
    ad = ad + (n-m+2)*(avg)
    return ad

def testMathAd(r):
    n = len(r)
    m = getMofY(r)
    avg = statistics.mean(r)
    floor = math.floor(avg)
    x = (-((floor-m+2)*(floor+m-1)/2)-(m-2-floor)*avg-((floor*(floor+1))/2) + floor*avg+(n-m+2)*avg)
    x = floor*(-(floor+m-1)/2+(m-2)/2+2*avg-(floor+1)/2)+2*avg*(n-m+2)
    return floor*(2*avg-floor-1)+ 2*avg*(n-m+2)

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
    