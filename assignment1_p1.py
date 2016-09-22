

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
    if r in q.keys():
        return False
    else:
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
            if (d[0]!='0' and d!=y  and isprime(int(float(d))) and notvisited(d,p)):
                listPrimes.append(d)
        i=i+1
    #make a list of all the primes less than x
    #return the list
    return listPrimes



def getPath(startP, endP):
    explore = dict()
    queue = []
    path=[]
    if(startP==endP):
        return startP
    queue.append(startP)
    explore[startP]=None
    while (not len(queue)==0):
        node = queue.pop(0)

        adjacent = getPossibleActions(node,explore)
        for a in adjacent:
            explore[a]=node
            if(a == endP):
                break
            queue.append(a)
                
    if(endP not in explore.keys()):
        return "UNSOLVABLE"
    while (explore[endP]!=None):
        path.append(endP)
        endP=explore[endP]
    path.append(startP)
    path.reverse()
    return path



def main():
    for line in sys.stdin.readlines():
        primes=str(line).split()
        q=getPath(primes[0],primes[1])
        if (q[-1] != primes[1]):
            print "UNSOLVABLE"
        else:
            print ' '.join(q)



if __name__=='__main__':
    main()





