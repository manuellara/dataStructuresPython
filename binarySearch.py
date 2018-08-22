# Binary Search 
# runtime of O( nlog(n) ) 
# runs best on ALREADY SORTED ARRAY
def binarySearch( arr , value ):

    if len( arr ) == 0 or ( len( arr) == 1 and arr[0] != value ):
        return False

    mid = arr[ len( arr ) // 2 ]

    if value == mid: 
        return print( value )

    if value < mid:
        return binarySearch( arr[ :len(arr) // 2 ] , value )

    if value > mid:
        return binarySearch( arr[ len(arr) // 2 + 1: ] , value )
