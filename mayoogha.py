#!/usr/bin/env python
# coding: utf-8

# In[ ]:



min_num=int(input("Enter the minimum number: "))
max_num=int(input("Enter the maximum number: "))
disabled_num={2,4,5,6,8,10}
# size=int(input("Enter the number of elements in the set: "))
# for i in range(size):
#     element=int(input("Enter the element: "))
#     disabled_num.add(element)
print("disabled number:",disabled_num)

validate=int(input("Enter the number to validate: "))

def val(validate):
    if validate not in range(min_num,max_num+1):
        print("Invalid Input")
    else:
        if validate in disabled_num:
            validate=validate+1
            val(validate)
        else:
            print(validate)
val(validate)
            

        
    


# In[ ]:





# In[ ]:





# In[ ]:




