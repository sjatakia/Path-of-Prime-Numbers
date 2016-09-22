

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





def getPath(startP, endP):
    # maintain a queue of paths
    explore1=[]
    explore2=[]
    queue1 = []
    queue2 = []
    path1=[]
    path2=[]
    # push the first path into the queue
    queue1.append([str(startP)])
    queue2.append([str(endP)])
    while ((len(queue1)!=0) and (len(queue2)!=0)):
        if(len(queue1)!=0):
            path1 = queue1.pop(0)
            node1 = path1[-1]
            explore1.append(node1)
            if (node1 == endP or (not notvisited(node1,explore2))):
                path=[path1,path2]
                return path
            adjacent1 = getPossibleActions(node1,explore1)
            for a in adjacent1:
                new_path1 = list(path1)
                new_path1.append(a)
                queue1.append(new_path1)
                
        if(len(queue2)!=0):
            path2 = queue2.pop(0)
            node2 = path2[-1]
            explore2.append(node2)
            if (node2 == startP or (not notvisited(node2,explore1))):
                path=[path1,path2]
                return path2
            adjacent2 = getPossibleActions(node2,explore2)
            for a in adjacent2:
                new_path2 = list(path2)
                new_path2.append(a)
                queue2.append(new_path2)
    path=[path1,path2]
    return path



def main():
    for line in sys.stdin.readlines():
        primes=str(line).split()
        q=getPath(primes[0],primes[1])
        if (len(q[0])==0 or len(q[1])==0 or q[0][-1]!=primes[1] or q[1][-1]!=primes[0]):
            print "UNSOLVABLE"
        else:
            print ' '.join(q[0])
            print ' '.join(q[1])

    
if __name__=='__main__':
    main()





