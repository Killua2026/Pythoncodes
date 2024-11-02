# x = """
#     this
#     is
#     me
#     """
# print(x)

# a=5
# while a!=0:
#     a-=1
#     if a==1:
#         continue
#     print(f'The value of a is{a}')
    
# name='value'
# for i in name:
#     print(i)

def countdown(a,in_0):
    if in_0 == True:
        while a!=0:
         a-=1
        print(f'The value of a is {a},{in_0}')
    
    elif in_0==False:
        while a!=1:
         a-=1
        print(f'The value of a is {a}')
        
        
     
print(countdown(5,False))     
    