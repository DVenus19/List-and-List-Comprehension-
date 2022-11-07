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
          "7. - Maximum and Minimum of the list1\n"
          "8. - Exit\n")
print("\n\t", list1)
menu()
option = int(input("Enter your option: "))

while option !=0:
    if option == 1:
        #add an element
        for item in list1:
            print(item)
            list1.append(int(input("\n\t Enter a number that you want to add: ")))
            print(list1)
            break
        
    elif option == 2:
        #insert an element
        insert = int(input("\n\t input the element that you want to insert: "))
        index = int(input("\t input the position you want: "))
        list1.insert(index-1,insert)
        print(list1)
        
        
    elif option == 3:
        #Modify an element
        element = int(input("\tinput the element that you want to modify/change: "))
        change = int(input("\t input an element you want to put in list1: "))
        for i in range(len(list1)):
            if list1[i]== element:
                list1[i] = change
        print(list1)
        
        
        
    elif option == 4:
        #Delete an element
        for item in list1:
            print(item)
        element = int(input("\n\t input the element you want to delete/remove: "))
        for i in range(len(list1)):
            error = 0 
            break
        else:
            error = 1 
        if error == 0 :
            list1.remove(element)
        else:
            print("The element is no longer in the list1")
        print(list1)
        
            
    elif option == 5:
        #arrange in ascending order
        list1.sort()
        print(list1)
        
        
    elif option == 6:
        #arrange in descending order
        list1.sort()
        list1.reverse()
        print(list1)

        
    elif option == 7:
        Largest = max(list1)
        Smallest = min(list1)
        print("The smallest element is : ", Smallest)
        print("The largest ele,element is : " ,Largest)
        print(list1)
        
    elif option == 8:
        print("Thank you, goodbye!")
        exit()
    else:
        print("Invalid option,please try again!!!")
        
    print()
    menu()
    option = int(input("Enter your option: "))


    
