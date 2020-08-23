def insert():
    print("Enter your name")
    User_Name =  input()
    print("Enter your phone num")
    User_Num = input()
    Names.append(User_Name)
    Phone_Numbers.append(User_Num)

def find():
    print("Enter your name")
    User_Name =  input()
    count = 0
    for Gowris in name:
     if Gowris == User_Name:
        print("Found") 
        print(phone[count])
     else:
        print("Not FOund")
     count = count + 1    
    
Names = ["Praveen","BadBoy","Badfy",]
Phone_Numbers = ["786872134","6876812736","76351267351"]
user_input = input()

if user_input == "X":
    insert()
if user_input == "Y":
    find()
