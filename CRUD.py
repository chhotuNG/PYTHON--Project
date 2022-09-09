d = {"chhotu": {"email": "cksurya7319@gmail.com", "age": 17, "roll no": 12, "phone number": 7464655655, },
     "saurabh": {"email": "saurabh@gmail.com", "age": 17, "roll no": 10, "phone number": 7464650090}}
l1 = ["email ", "age", "roll_no", "phone number"]
while True:
    print("""
1) create
2) read
3) update
4) delete""")
    n1 = input("please select what you want >> ")
    if n1 == "1":
        while True:
            d1 = {}
            n2 = input("enter student name >> ")
            for i in l1:
                n3 = input(f"enter {i} of student >>> ")
                d1[i] = n3
            d[n2] = d1
            n4 = input("you want to add more y/n >> ")
            if n4 == "n":
                print(d)
                break
            else:
                continue
    elif n1 == "2":
        n4 = input("enter student name which you want to read >>  ")
        if n4 in d:
            print(n4, end=" ")
            print(d[n4])
        else:
            print("student not found ")
    elif n1 == "3":
        n5 = input("enter student name which you want to update >>  ")
        if n5 in d:
            print(n5, end=" ")
            b = d[n5]
            n6 = input("Do you want to change student name y/n >> ")
            if n6 == "y":
                n7 = input("enter changing name of student >> ")
                del d[n5]
                d[n7] = b
                print("what you want update")
                for i in l1:
                    print(i)
                n8 = input("select one >>")
                if n8 == "email":
                    n9 = input("enter changing email of student >> ")
                    d[n7][n8] = n9
                elif n8 == "age":
                    n10 = int(input("enter student changing age >> "))
                    d[n7][n8] = n10
                elif n8 == "roll_number":
                    n11 = int(input("enter roll changing number"))
                    d[n7][n8] = n11
                elif n8 == "phone number":
                    n12 = int(input("enter changing phone number >> "))
                    d[n7][n8] = n12
            else:
                print("what you want update ")
                for i in l1:
                    print(i)
                n8 = input("select one >>")
                if n8 == "email":
                    n9 = input("enter changing email of student >> ")
                    d[n5][n8] = n9
                elif n8 == "age":
                    n10 = int(input("enter student changing age >> "))
                    d[n5][n8] = n10
                elif n8 == "roll_number":
                    n11 = int(input("enter roll changing number"))
                    d[n5][n8] = n11
                elif n8 == "phone number":
                    n12 = int(input("enter changing phone number >> "))
                    d[n5][n8] = n12
    elif n1 == "4":
        n4 = input("enter student name which you want delete >> ")
        del d[n4]
    else:
        print("not data found ")
        break
print(d)
