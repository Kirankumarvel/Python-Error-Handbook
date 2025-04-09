nums = [1,2,3]
#print(nums[5]) # Attempting to access an index that doesn't exist
#IndexError: list index out of range

if len(nums) > 5:
    print(nums[5])  # This will not be executed because the condition is false  
else:
    print("Index out of range")