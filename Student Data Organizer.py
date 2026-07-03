#start with welcome message
print("Welcome to the Student Data Organizer !  ")

# make empty list for store students data 
students = []

while True:
    print("\nSelect an option : ")

    print("\n1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        print("\nEnter student details : ")

        # making id inout in while loop bcz .  when user input mistakely string , ect. get error . and print please enter numbers only.
        while True:
            Id = input("Enter 2 digit Id : ")

            if Id.isdigit():
                if 10 <= int(Id) <= 99:
                    iD = int(Id)
                    break
                else:
                    print("error : Enter number between 10 to 99 ! ")
            else:
                print("error : Please enter only numbers")

        name = input("Student name : ")
        # same if user make mistake like id .
        while True : 
            age = input("Age : ")
            if age.isdigit():
                Age = int(age)
                break
            else:
                print("error : Please enters only numbers")

        grade = input("Grade : ")
        dob = input("Date of Birth (YYYY-MM-DD) : ")
        subject = set(x.strip() for x in input("Subject (comma - separated) : ").split(","))

        #add id and date of birth in tuple 
        info = (iD , dob)
        # sub_set = {subject}

        # store student data in list
        student = {"student_info" : info,
                   "Name" : name,
                   "Age" : age,
                   "Grade" : grade,
                   "Subjects" : subject
                   }
        students.append(student)

    elif choice == "2":
        print("\nDisplay All Students : ")

        if len(students)==0:
            print("\nNot added any students information!")

        else:
            for s in students :
                ID = s["student_info"][0]
                DOB = s["student_info"][1]
                print(f"\nID : {ID}")
                print("Students Name : {}".format(s["Name"].title()))
                print("Date of Birth (YYYY-MM-DD) : {}".format(DOB))
                print("Age : %s" % s["Age"])
                print("Grade : %s" % s["Grade"].upper())
                print("Subjects : {}".format(s["Subjects"]).title())
        
    elif choice =="3" :
        #If user want to change any details in list
        search_id = int(input("\nStudent ID : "))
        for s in students:
            ID = s["student_info"][0]

            if search_id == ID :
                s["Name"] = input("Update Name : ")
                s["Age"] = int(input("Upadte Age : "))
                s["Grade"] = input("Update Grade : ")
                s["Subjects"] = input("Update Subjects : ")

                print("Update Successfully.")

            else:
                print("\nEntered student ID is invaid!")

    elif choice == '4':
        #if any user want to delete any students details so delete with search by student id.
        print("\nDelete Student :")

        search_id = int(input("\nStudent ID : "))

        for s in range(len(students)):
            if search_id == students[s]["student_info"][0]:
                del students[s]
                print("\nStudent Details Deleted.")
            else:
                print("\nNot Found Student ID, Try Again!")

    elif choice == "5":
        print("\nDisplay Subjects Offered")

        for s in students:
            print(f"{s["Name"]} | {s["Subjects"]}")

    elif choice == "6":
        print("\nThank you, For using this wonderfull Students Data Organizer!")
        break
    
    else :
        print("\nError!!")

    



        
    