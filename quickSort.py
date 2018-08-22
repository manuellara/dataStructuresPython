#Quick Sort 
#runtime O( nlog(n) )
#space complexity is O( log(n) )
#BAD WITH LARGE DATA SETS
def quickSort( a ):

    if len( a ) <= 1:
        return a

    smaller , equal , larger = [] , [] , []

    pivot = a[ randint( 0 , len( a ) - 1 ) ]

    for x in a:
        if x < pivot:
            smaller.append( x )
        elif x == pivot :
            equal.append( x )
        else:
            larger.append( x )

    return quickSort( smaller ) + equal + quickSort( larger )