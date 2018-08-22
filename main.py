from random import randint

def createList( size=100 , max=100 ):
    return [ randint(0 , max) for i in range( size )]



#Binary Search driver code
#import binarySearch

#sortedArr = []
#for i in range( 1, 1000 ):
#    sortedArr.append(i)

#binarySearch( sortedArr , 799 )

###############################################################

#Bubble Sort driver code
#from bubbleSort import *

#a = createList()

#print( bubbleSort( a ) )

###############################################################

#Quick Sort driver code
#from quickSort import *

#a = createArray()
#print( "Unsorted Array = " , a )

#sortedArr = quickSort( a )
#print( "Quick Sortted Array = " , sortedArr  )

###############################################################

#Merge Sort driver code
#from mergeSort import *

#a = createArray()
#print( "Unsorted Arry" , a )

#sortedArr = mergeSort( a )
#print( "Merge Sorted Array" , sortedArr )

###################################################################################################################################################

#BFS :: Breadth First Search 
#from BFS import *

#g = Graph()

#a = Vertex( 'A' )

#g.addVertex( a )

#for i in range( ord('A') , ord('K') ):
#    g.addVertex( Vertex( chr(i) ) )

#edges = [ 'AB' , 'AE' , 'BF' , 'CG' , 'DE' , 'DH' , 'EH' , 'FG' , 'FI' , 'FJ' , 'GJ' , 'HI' ]

#for edge in edges:
#    g.addEdge( edge[:1] , edge[1:] )

#g.bfs( a )
#g.printGraph()


###################################################################################################################################################

#Binary Search Tree
#from BST import *

#arr = createList()

#bst = Tree()

#for i in arr:
#    bst.insert( i )

#bst.inorder()


###############################################################

#Linked List
from linkedList import *

myList = linkedList()

a = createList()

for i in a:
    myList.append( i )

myList.display()

print( "index at 2nd index : {}".format( myList.get(2) )  )

myList.delete( 2 )

myList.display()



