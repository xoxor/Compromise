import sys, os, statistics, math

def main():
    proposition = True
    for m in range(4,1000):
        low = max(4,m-1)
        print(m,low)
        for n in range (low,1000):
            x = generateX(m,n)
            y = generateY(m,n)
            proposition = checkProposition(x,y)
            if not proposition :
                print("FAIL: m ",m," n ",n)
                return

def meanAbsDiff(r):
    n=len(r)
    mad=0
    for i in range(n):
        for j in range(n):
            mad = mad + abs(r[i] - r[j])
    return mad/(n^2)

def avgAbsDev(r):
    n = len(r)
    avg = statistics.mean(r)
    ad=0
    for i in range(n):
        ad = ad + abs(r[i] - avg)
    return ad/n

def stDev(r):
    n = len(r)
    avg = statistics.mean(r)
    sd = 0
    for i in range(n):
        sd = sd + math.pow(r[i] - avg,2)
    return math.sqrt(sd/n)

def gini(r):
    n = len(r)
    summ = sum(r)
    g = 0
    for i in range(n):
        for j in range(n):
            g = g + abs(r[i] - r[j])
    return g/(2*n*summ)

def checkProposition(x,y):
    flag = True
    if (meanAbsDiff(x)>meanAbsDiff(y)):
        print(x,y,"meanAbsDiff")
        flag = False
    if (avgAbsDev(x)>avgAbsDev(y)):
        print(x,y,"avgAbsDev")
        flag = False
    if (stDev(x)>stDev(y)):
        print(x,y,"stDev")
        flag = False
    if (gini(x)>gini(y)):
        print(x,y,"gini")
        flag = False
    return flag

def generateX(m,n):
    r=[]
    r.append(m-3)
    r.append(m-1)
    for i in range(n-2): 
        r.append(m-2)
    return r


def generateY(m,n):
    r=[]
    for i in range(m-2): 
        r.append(m-2-i)
    for i in range(n-m+2): 
        r.append(0)
    return r

# old utility methods 
def getMofY(rY):
    return rY[0]+2

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
    return sum/(n^2)




if __name__ == "__main__":
    main()
    