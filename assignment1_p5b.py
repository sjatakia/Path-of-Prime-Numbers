


__author__ = 'sjatakia@ucsd.edu, A11555559, krkelkar@ucsd.edu, A12045566, apbhulla@ucsd.edu, A10624774'

import sys
is_py2 = sys.version[0]=='2'
if is_py2:
    import Queue as queue
else:
    import queue as queue

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

def heuristicCost(currPath,str_current,str_goal):
    count = 0
    if(len(str_current)!= len(str_goal)):
        count = 10000
        return count
    for index in range(0,len(str_goal)):
        if(str_current[index] != str_goal[index]):
            count += int(str_current[index]) + int(str_goal[index])
    return count + (len(currPath)-1)

def getPath (startP, endP ) :
    explore = []
    que = queue.PriorityQueue()
    que.put((0,[str(startP)]))
    while not que.empty():
        path = (que.get())[1]
        node = path[-1]
        explore.append(node)
        if node == endP:
            return ' '.join(path)
        adjacent = getPossibleActions(node, explore)
        for a in adjacent:
            new_path = list(path)
            new_path.append(a)
            cost = heuristicCost(new_path, a, endP)
            que.put((cost, new_path))
    return 'UNSOLVABLE'
 

def main():
      for line in sys.stdin.readlines():
            primes=str(line).split()
            print(getPath(primes[0],primes[1]))
if __name__ =='__main__':
    main()




