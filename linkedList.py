#Linked List

class node:

    def __init__( self , data = None ):
        self.data = data
        self.next = None

class linkedList:

    def __init__( self ):
        self.head = node()

    def append( self , data ):
        newNode = node( data )
        cur = self.head

        while cur.next != None:
            cur = cur.next

        cur.next = newNode 

    def length( self ):
        cur = self.head
        
        total = 0

        while cur.next != None:
            total += 1
            cur = cur.next

        return total

    def display( self ):
        elems = []

        cur = self.head

        while cur.next != None:
            cur = cur.next
            elems.append( cur.data )

        print( elems )

    def get( self , index ):
        if index >= self.length():
            print( "ERROR: Index out of range..." )
            return None

        curIDX = 0
        cur = self.head

        while True:
            cur = cur.next

            if curIDX == index:
                return cur.data
            
            curIDX += 1

    def delete( self , index ):
        if index >= self.length():
            print( "ERROR: Index out of range..." )
            return

        curIDX = 0
        cur = self.head

        while True:
            prev = cur
            cur = cur.next

            if curIDX == index:
                prev.next = cur.next
                return

            curIDX += 1
