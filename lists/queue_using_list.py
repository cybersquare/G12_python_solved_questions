# Write a Python program to implement a queue using a listdata-structure. 
queue = []
c = 'y'
while c == 'y':
   print('1. Insert')
   print('2. Delete')
   print('3. Display')
   choice=int(input('Please enter your choice: '))
   if choice == 1: # Add element
       elem=input('Enter new element: ')
       queue.append(elem)
   elif choice == 2: # Delete element
       if queue == []:
           print('Queue is empty')
       else:
           print('deleted element is:', queue[0])
           del queue[0]
   elif choice == 3: # View elements
       l=len(queue)
       for i in range(0,l):
           print(queue[i])
   else:
       print('Wrong input')
   c=input('Do you want to continue(y/n): ')