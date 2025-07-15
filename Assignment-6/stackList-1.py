class Stack ( object ):
    def __init__ ( self ):
        """
        Purpose
        initializes an empty Stack object
        """
        self . __data = list ()
    def is_empty ( self ):
        """
        Purpose
        checks if the stack has no data in it
        Return :
        True if the stack has no data , or false otherwise
        """
        return len ( self . __data ) == 0
    def size ( self ):
        """
        Purpose
        returns the number of data values in the stack
        Return :
        The number of data values in the stack
        """
        return len ( self . __data )
    def push ( self , value ):
        """
        Purpose
        adds the given data value to the stack
        Pre - conditions :
        value : data to be added
        Post - condition :
        the value is added to the stack
        Return :
        ( none )
        """
        self.__data.append (value)
    def pop ( self ):
        """
        Purpose
        removes and returns a data value from the stack
        Post - condition :
        the top value is removed from the stack
        Return :
        returns the value at the top of the stack
        """
        return self.__data.pop()
    def peek( self ):
        """
        Purpose
        returns the value from the front of stack
        without removing it
        Post - condition :
        None
        Return :
        the value at the front of the stack
        """
        return self.__data [ -1]