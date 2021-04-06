"""
Text Type:    str
Numeric Types:    int, float, complex(º¹¼Ò¼ö)
Sequence Types:    list, tuple, range
Mapping Type:    dict
Set Types:    set, frozenset
Boolean Type:    bool
Binary Types:    bytes, bytearray, memoryview
In Python, the data type is set when you assign a value to a variable:
"""
x = list(("apple", "banana", "cherry"))  # list    
print(x)
x = tuple(("apple", "banana", "cherry"))  #  tuple
print(x)
x = range(6)
print(x)
x = dict(name="John", age=36)    #dict    
print(x)
x = set(("apple", "banana", "cherry"))   # set    
print(x)
x = frozenset(("apple", "banana", "cherry"))    #frozenset   
print(x) 
x = bool(5)    #bool    
print(x)
x = bytes(5)    #bytes    
print(x)
x = bytearray(5)    #bytearray    
print(x)
x = memoryview(bytes(5))   # memoryview
print(x)
