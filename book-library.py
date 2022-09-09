lib_student = {"chhotu": [{"THE MAGIC": 1}],
               "bansi": [{"THE WORLD": 2, "THE HAPPYINESS": 1}]}
liberary = {"DARKNESS AT NIGHT": 4, "THE SUN ": 6, "THE EARTH": 8, "THE VILLAGER": 4,
            "THE MAHATMA GANDHI": 10, "THE MAGIC": 3, "THE WORLD": 5, "THE HAPPYINESS": 3}
print(liberary)
while True:
    name = input("ENTER YOUR NAME______: ")
    choice = input("WHAT YOU WANT return / purches/quite to liberary_____: ")
    if choice == "return":
        if name in lib_student:
            print("you returnig the book \n thank you!! ")
            book = input("ENTER THE NAME OF BOOK______: ")
            q = int(input("ENTER NO. OF BOOK YOU WANT TO RETURN____: "))
            book = book.upper()
            if book in liberary:
                liberary[book] = liberary[book]+q
                print("THANKS FOR VISITING !!!!")
                print(liberary)
                lib_student.pop(name)
                print(lib_student)
            else:
                print("SORRY BOOK NOT IN AVAILABLE IN LIBERARY ")
        else:
            print(
                " YOU'R DATA NOT FOUND IN LIST \n MAYBE YOU DIDN'T TAKE BOOK\n THANK YOU!!!")
    elif choice == "purches":
        if name not in lib_student:
            book = input("ENTER BOOK NAME______: ")
            book = book.upper()
            n = int(input("HOW MANY BOOK YOU WANT______: "))
            if book in liberary and n <= liberary[book] and liberary[book] != 0:
                lib_student[name] = [{book: n}]
                liberary[book] = liberary[book]-n
                print(lib_student)
                print(liberary)
                continue
        else:
            print("YOU ALREADY TAKE BOOK", lib_student[name],)
            print("IF YOU WANT TO PURCHESE ANOTHER y/n::::")
            s = input("__________:")
            if s == "y":
                print("ENTER YOU'R NAME____: ")
                name = input("________: ")
                book = input("ENTER BOOK NAME______: ")
                book.upper()
                if book in liberary:
                    y = 0
                    n = int(input("HOW MANY BOOK YOU WANT______: "))
                    for k, v in lib_student.items():
                        if k == name:
                            for x in lib_student[name]:
                                for k, v in x.items():
                                    if book == k:
                                        re = v+n
                                        lib_student[name][y][k] = re
                                        if liberary[book] > 0:
                                            liberary[book] -= n
                                            print(
                                                "PURCHES SUCCESSFUL \n CONGRTATULATION !!!!")
                                            y += 1
                                            print(liberary)
                                            print(lib_student)
                                        else:
                                            print(
                                                "THIS BOOK IS OUT OF STOKE !!! \n SORRY !!!")
                else:
                    print("you enterted something wrong!!!!!")

            else:
                print("thanks for visiting !!!")
                break
    elif choice == "quite":
        print("thanks for visiting !!!")
        break
    else:
        print("you enter something wrong !!!")
