# Write a Python program to implement a queue using a list data-structure. 

stack=[]
c='y'
while (c=='y'):
   print('1. PUSH')
   print('2. POP ')
   print('3. Display')
   choice=int(input('Enter your choice: '))
   if (choice==1): # Push
       a=int(input('Enter any number :'))
       stack.append(a)
   elif (choice==2): # Pop
       if (stack==[]):
           print('Stack is Empty')
       else:
           print('Deleted element is :',stack.pop())
   elif (choice==3): # Display
       l=len(stack)
       for i in range(l-1,-1,-1):
           print(stack[i])
   else:
       print('Wrong Input')

   c=input("Do you want to continue or not? ")
