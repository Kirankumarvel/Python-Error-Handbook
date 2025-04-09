num =5
#num.append(5) # Attempting to call a method that doesn't exist on an integer
# AttributeError: 'int' object has no attribute 'append'
# The AttributeError occurs when you try to access an attribute or method that doesn't exist for a particular object.   
# In this case, the append method is not defined for integers, which is why the error occurs.
# To avoid this error, make sure you are using the correct object type and method.        
#   # For example, if you want to append a value to a list, you should first create a list: 
#   my_list = [1, 2, 3]
#   my_list.append(4)  # This will work because append is a valid method for lists
#   # If you want to add a value to an integer, you can use the + operator:     
#   num = 5
#   num += 5  # This will work because you are using the + operator to add 5 to the integer num
#   #   # In summary, make sure you are using the correct object type and method to avoid AttributeError.   
lst =[]
lst.append(5) # This will work because append is a valid method for lists     
print(lst)  # Output: [5]