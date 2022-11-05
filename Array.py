print("LAB EXERCISE ")
print("PROGRAMMED BY : DONASCO,VENUS M.")
print("BSCOE 2-2 ")
list1 = [10,30,20,50,40,60,90,100,70,80]
def menu() :
        print("\n\n----------------------------- What do you like to do?--------------------------------\n\n"
          "1. - Add an element \n"
          "2. - Insert an element \n"
          "3. - Modify an element \n"
          "4. - Delete an element\n"
          "5. - Arrange in ascending order\n"
          "6. - Arrange in descending order\n"
          "7. - Exit\n")

menu()
option = int(input("Enter your option: "))

while option !=0:
    if option == 1:
        #add an element
        for item in list1:
            print(item)
            list1.append(110)
            print(list1)
            break
        
    elif option == 2:
        #insert an element
        for item in list1:
            print(item)
            list1.insert(3,0)
            print(list1)
            break
        
    elif option == 3:
        #Modify an element
        for item in list1:
            print(item)
            list1[4]=120
            print(list1)
            break
        
    elif option == 4:
        #Delete an element
        for item in list1:
            print(item)
            list1.remove(30)
            print(list1)
            break
            
    elif option == 5:
        #arrange in ascending order
        for item in list1:
            print(item)
            list1.sort()
            print(list1)
            break
        
    elif option == 6:
        #arrange in descending order
        for item in list1:
            print(item)
            list1.sort()
            list1.reverse()
            print(list1)
            break
    
    elif option == 7:
        print("Thank you, goodbye!")
        exit()
    else:
        print("Invalid option,please try again!!!")
        
    print()
    menu()
    option = int(input("Enter your option: "))


    
