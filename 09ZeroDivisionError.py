#x = 10/0 
x=10 
# #ZeroDivisionError: division by zero
#print(x)
y=0

if y != 0:
    x = 10 / y  # This will raise a ZeroDivisionError if y is 0
else:       
    print("y is zero, cannot divide by zero")
    y= 0       

# #ZeroDivisionError: division by zero

# print(x)
# # This will not be executed because the condition is false
# else:

#     print("Index out of range")
print(x)    
    
