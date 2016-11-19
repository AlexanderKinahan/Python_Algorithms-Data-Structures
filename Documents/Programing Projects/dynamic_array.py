##Alexander Kinahan 2016 

import ctypes      


class DynamicArray(object): 
    
    
    def __init(self):
        self.n = 0              
        self.capacity = 1 
        self.A = self.make_array(self.capacity)     ## makes an array of 0 elements and size 1
        
    #def__len__(self)     ## returns number of elements in self
    #return self.n 
    

    def __getitem__(self, k):     ## returns item at index in array A
        if not 0<= k < self.n: 
            return IndexError('K is out of bounds')
        return self.A[k] 
    
    
    def append(self, element): 
        if self.n == self.capacity: 
            self._resize(2*self.capacity)    # 2 times resize 
            
        self.A[self.n] = element
        self.n += 1 
        
    def _resize(self, new_cap): 
        B = self.make_array(new_cap)    ## TEMPORARY ARRAY b made 
        for k in range(self.n):           
            B[k] = self.A[k]           ## COPIES every element over 
            
        self.A = B 
        self.capacity = new_cap 
        
        
    def make_array(self, new_cap): 
        return (new_cap * ctypes.py_object)() 
        
