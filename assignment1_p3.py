


__author__ = 'sjatakia@ucsd.edu, A11555559, krkelkar@ucsd.edu, A12045566, apbhulla@ucsd.edu, A10624774'
import sys

def isprime(startnumber):
    startnumber*=1.0
    prime = True
    for divisor in range(2,int(startnumber**0.5+1)):
        if startnumber/divisor==int(startnumber/divisor):
            prime=False
    return prime



def notvisited(r,q):
    for w in q:
        if w==r:
            return False
    return True



def getPossibleActions(x,p):
    #remove all the elements that are not approachable from x
    listPrimes=[]
    y = str(x)
    #print y
    i=1
    for c in y:
        for s in range(0,10):
            d = y[0:i-1] + str(s) + y[i:]
            if (d[0]!='0' and d!=y and notvisited(d,p) and isprime(int(float(d)))):
                listPrimes.append(d)
        i=i+1
    #make a list of all the primes less than x
    #return the list
    return listPrimes



def getPathHelper(startP, endP, limit, path,explore):
    if (startP == endP):
        path.append(endP)
        return path
    elif(limit==0):
        return path
    else:
        explore.append(startP)
        adjacent = getPossibleActions(startP,explore)
        path.append(startP)
        for a in adjacent:
            result = getPathHelper(a, endP,limit-1,path,explore)
            if (result[len(result)-1] == endP):
                return result
        explore.pop()
        path.pop()
        return path



def getPath(startP,endP,depth):
    for i in range(0,depth+1):
        path = getPathHelper(startP,endP,i,[],[])
        if(len(path)!=0):
            return path
    return []



def main():
    for line in sys.stdin.readlines():
        primes=str(line).split()
        q=getPath(primes[0],primes[1],8)
        if (len(q)==0):
            print "UNSOLVABLE"+"\n"
        else:
            print ' '.join(q)

    
if __name__=='__main__':
    main()



