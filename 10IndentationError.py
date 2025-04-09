def greet():
#print("Hello")  # IndentationError: expected an indented block
    print("Hello")  # Correct indentation
greet()  # Call the function to see the output
# Output:       
# Hello
# The code above demonstrates an IndentationError in Python.    
# Indentation is crucial in Python as it defines the structure and flow of the code.
# In this case, the error occurs because the print statement inside the greet function is not properly indented.        
# To fix the error, we need to indent the print statement correctly.
# By adding the correct indentation, the code will run without any errors and produce the expected output.
# IndentationError occurs when there is an issue with the indentation of your code. 
# Python relies on indentation to define the structure of the code, such as loops, conditionals, and function definitions.
# If the indentation is inconsistent or incorrect, Python will raise an IndentationError.
# To fix this error, make sure that all your code blocks are properly indented and consistent.
# Here are some common causes of IndentationError:

# 1. Mixing tabs and spaces: Make sure you are using either tabs or spaces for indentation, not both.
#    Python recommends using 4 spaces for indentation.
# 2. Incorrect indentation level: Ensure that all lines of code within the same block have the same indentation level.
# 3. Missing indentation: If you have a block of code that should be indented (e.g., inside a function or loop), make sure to indent it properly.
# 4. Extra indentation: If you have an extra indentation level that doesn't match the surrounding code, it will raise an IndentationError.
# 5. Inconsistent indentation: Ensure that all lines of code within the same block have the same indentation level.