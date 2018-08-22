#Binary Search Tree
#O( h )  ::  h = height of tree
class Node:

    def __init__( self , val ): #initializes node
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert( self , data ):
        if self.value == data: # if node value == data, does not add
            return False

        elif self.value > data: #if data less than curr node value, traverse left
            if self.leftChild:
                return self.leftChild.insert( data )
            else:
                self.leftChild = Node( data )
                return True

        else: #if data greater than curr node value, traverse right
            if self.rightChild:
                return self.rightChild.insert( data )
            else:
                self.rightChild = Node( data )
                return True

    def find( self , data):
        if self.value == data: #if data == value, we found our node
            print( "Node " , data , " was found!" )
            return True
        elif self.value > data: #if data less than curr node, traverse left
            if self.leftChild:
                return self.leftChild.find( data )
            else:
                return False
        else: #if data greater than curr node, traverse left
            if self.rightChild:
                return self.rightChild.find( data )
            else:
                return False

    def preorder( self ):                       #DEPTH FIRST SEARCH
        if self:
            print( str( self.value ) ) #process node first

            if self.leftChild:
                self.leftChild.preorder()

            if self.rightChild:
                self.rightChild.preorder()

    def postorder( self ):                      #DEPTH FIRST SEARCH
        if self:
            if self.leftChild:
                self.leftChild.postorder()

            if self.rightChild:
                self.rightChild.postorder()
                
                print( str( self.value ) ) #process node last

    def inorder( self ):                        #DEPTH FIRST SEARCH
        if self:
            if self.leftChild:
                self.leftChild.inorder()

            print( str( self.value ) ) #process node in-order

            if self.rightChild:
                self.rightChild.inorder()



class Tree:

    def __init__( self ): #initializes root to none
        self.root = None

    def insert( self , data ): #adds data to tree
        if self.root:
            return self.root.insert( data )
        else: #if root doesnt exist, root is created
            self.root = Node( data )
            return True

    def find( self , data ):
        if self.root: #if root exists, pass data to be searched for
            return self.root.find( data )
        else:
            return False

    def preorder( self ):
        print( "PreOrder" )
        self.root.preorder()

    def postorder( self ):
        print( "PostOrder" )
        self.root.postorder()

    def inorder( self ):
        print( "InOrder" )
        self.root.inorder()