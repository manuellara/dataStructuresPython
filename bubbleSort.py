#Bubble Sort
#Runtime :: O( n ) 
#Space Complexity :: O( 1 )
#good for small lists

def bubbleSort( list ):
    for i in range( 0 , len( list )-1 ):
        for j in range( 0 , len( list ) - 1 - i ):

            if list[ j ] > list[ j+1 ]:
                list[ j ] , list[ j+1 ] = list[ j+1 ] , list[ j ]

    return list