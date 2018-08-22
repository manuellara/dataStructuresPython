#Merge Sort 
#runtime O( nlog(n) )
#space complxity O(n)
#GOOD WITH LARGE DATA SETS
def merge( a , b ):

    c = []
    a_idx , b_idx = 0 , 0

    while a_idx < len( a ) and b_idx < len( b ):
        if a[ a_idx ] < b[ b_idx ]:
            c.append( a[ a_idx ] )
            a_idx += 1
        else:
            c.append( b[ b_idx ] )
            b_idx += 1

    if a_idx == len( a ):
        c.extend( b[ b_idx: ] )
    else:
        c.extend( a[ a_idx: ] )

    return c

def mergeSort( a ):
    
    if len( a ) <= 1: return a

    left , right = mergeSort( a[ :len(a) // 2 ] ) , mergeSort( a[ len(a) // 2: ] )
    
    return merge( left , right ) 
