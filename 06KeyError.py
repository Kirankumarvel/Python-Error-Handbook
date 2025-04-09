data = {'a':1, 'b':2, 'c':3}
#print(data['b'])
# KeyError: 'b' not found in dictionary
# The KeyError occurs when you try to access a dictionary key that doesn't exist.   
# In this case, 'b' is not a key in the dictionary data, which only contains 'a'.
# To avoid this error, you can use the get method, which returns None (or a default value) if the key is not found. 
# For example:      
# print(data.get('b'))  # This will return None instead of raising an error
# You can also provide a default value to return if the key is not found:
# print(data.get('b', 'Key not found'))  # This will return 'Key not found' instead of raising an error
# This way, you can handle missing keys gracefully without causing a KeyError.  
print(data.get('d', 'Key not found'))