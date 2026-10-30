
students = []

while True:
    print("=" * 90)
    print("            Student Management System")
    print("=" * 90)
    print("                 Main Menu")
    print("=" * 90)
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Result")
    print("99. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        print("\n------ Add Student ------")
        roll = input("Enter Roll No : ")
        name = input("Enter Name : ")
        age = input("Enter Age : ")
        marks = float(input("Enter Marks : "))

        student = {
            "roll": roll,
            "name": name,
            "age": age,
            "marks": marks
        }

        students.append(student)
        print("\nStudent Added Successfully!")

    elif choice == "2":
        print("\n------ Student List ------")

        if len(students) == 0:
            print("No Student Found!")

        else:
            for s in students:
                print("-" * 60)
                print("Roll No :", s["roll"])
                print("Name    :", s["name"])
                print("Age     :", s["age"])
                print("Marks   :", s["marks"])

    elif choice == "3":
        roll = input("Enter Roll No to Search : ")

        found = False

        for s in students:
            if s["roll"] == roll:
                print("\nStudent Found")
                print("Name :", s["name"])
                print("Age :", s["age"])
                print("Marks :", s["marks"])
                found = True

        if found == False:
            print("Student Not Found!")

    elif choice == "4":
        roll = input("Enter Roll No to Update : ")

        found = False

        for s in students:
            if s["roll"] == roll:
                s["name"] = input("Enter New Name : ")
                s["age"] = input("Enter New Age : ")
                s["marks"] = float(input("Enter New Marks : "))
                print("Student Updated Successfully!")
                found = True

        if found == False:
            print("Student Not Found!")

    elif choice == "5":
        roll = input("Enter Roll No : ")

        found = False

        for s in students:
            if s["roll"] == roll:
                print("\nName :", s["name"])
                print("Marks :", s["marks"])

                if s["marks"] >= 33:
                    print("Result : PASS")
                else:
                    print("Result : FAIL")

                found = True

        if found == False:
            print("Student Not Found!")

    elif choice == "99":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!")

    input("\nPress Enter to Continue...")