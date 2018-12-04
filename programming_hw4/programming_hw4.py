###########################################
#   107-1 Data Structure and Programming
#   Programming Assignment #4
#   Instructor: Pei-Yuan Wu
############################################

import sys
import pdb

# **********************************
# *  TODO                          *
# **********************************
'''
You need to complete this class MinBinaryHeap()
Feel free to add more functions in this class.
'''
class MinBinaryHeap():
    def __init__(self):
        self.heap = [0] # with a dummy node

    def insert(self, item):
        # TODO #
        self.heap.append(item)
        i = len(self.heap)-1
        self._insert(i)

    def deleteMin(self):
        # TODO #
        n = len(self.heap)-1
        self.heap[1]=self.heap[n]
        self.heap.pop()
        n = n-1
        if n > 0: self._adjust(1,n)

    def findMin(self):
        # TODO #
        return self.heap[1]

    def size(self):
        # TODO #
        return len(self.heap)-1
    
    def string(self):
        # Convert self.heap into a string
        return list2String(self.heap[1:])

    def _adjust(self, i ,n):
        k = self[i]
        j = 2 * i
        while j <= n:
            if j < n:
                if self[j] > self[j+1]: j = j+1
            if k <= self[j]: break
            else: 
                self[j/2] = self[j]
                j = 2 * j
        self[j/2] = k
    
    def _insert(self, i):
        while self[i] < self[i/2] and i/2 > 0:
            self[i], self[i/2] = self[i/2], self[i]
            i = i/2
    def __getitem__(self, key):
        return self.heap[key]

    def __setitem__(self,key,value):
        self.heap[key] = value

def list2String(l):
    formatted_list = ['{}' for item in l ] 
    s = ','.join(formatted_list)
    return s.format(*l)

if __name__ == '__main__':
    # 1. Check the command-line arguments
    #if len(sys.argv) != 3:
    #    sys.exit("Usage: python3 programming_hw4.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_line_list = list(inFile.read().splitlines())
    n = len(input_line_list)
    input_cmd_list = [ line.split(' ') for line in input_line_list ]
    inFile.close()

    # 3. Solve
    minPQ = MinBinaryHeap()
    findMin_list = []
    i = 0
    for cmd in input_cmd_list:
        if cmd[0] == 'insert':
            # print('insert {}'.format(cmd[1]))
            minPQ.insert(int(cmd[1]))
        elif cmd[0] == 'deleteMin':
            # print('deleteMin')
            if minPQ.size() > 0:
                minPQ.deleteMin()
        elif cmd[0] == 'findMin':
            # print('findMin')
            if minPQ.size() > 0:
                findMin_list.append(minPQ.findMin())
            else:
                findMin_list.append('-')
        else: # Unknown command
            assert False
        i = i+1
        print(i*100/n,"%")
        # print(minPQ.string())
    
    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    # 4.1 Output FindMin string
    outFile.write('{}\n'.format(list2String(findMin_list)))
    # 4.2 Output minPQ string
    outFile.write('{}'.format(minPQ.string()))
    outFile.close()

    # 5. Validation
    oFile = open(sys.argv[2], 'r')
    aFile = open(sys.argv[3], 'r')
    oFile_list = list(oFile.read().splitlines())
    aFile_list = list(aFile.read().splitlines())
    if oFile_list == aFile_list : print('correct')
    else : print('uncorrect')
