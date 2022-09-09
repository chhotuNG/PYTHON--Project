print("------WELCOME TO SBI ATM------")
pin = 1234
amount = 10000
chance = 3
card = input("press yes if the card insterted_____:  ")
card.upper()
if card == "yes" or card == "y":
    print("card inserted____")
    while True:
        p = int(input("enter you'r pin_____: "))
        if p == pin:
            print("corret pin_____")
            while True:
                print("""
press 1 for withdraw 
press 2 for deposite
press 3 for balance enquiry
press 4 for pin change
press 0 for quite """)
                sel_u = int(input("select you'r choice______: "))
                if sel_u == 1:
                    a1 = int(input("enter withdraw amount____: "))
                    if a1 < amount:
                        amount -= a1
                        print("""
                        withdraw successful !!!!
                        your current amount is """, amount)
                    else:
                        print("""maybe you enter more then current amount
                         We will suggest you check you'r balance """)
                elif sel_u == 2:
                    a1 = int(input("enter deposite amount____: "))
                    print("you'r current amount in you'r account is___:", amount+a1)
                elif sel_u == 3:
                    print("you'r current amount is____:", amount)
                elif sel_u == 4:
                    print("enter your old pin___:")
                    o_p = int(input("__________________: "))
                    if o_p == pin:
                        print("enter new pin")
                        n_p = int(input("_________: "))
                        print("enter again new pin for conform ")
                        a_n_p = int(input("__________:"))
                        if n_p == a_n_p:
                            pin = n_p
                            print("pin change successful !!!!")
                    else:
                        print("incorret password !!!")
                else:
                    print("thanks for coming come again !!!!")
                    break
        else:
            if chance != 0:
                print("you lost you'r chance !!!")
                print("please take you'r card ")
            else:
                print("you lost chance !!!")
                break
            print("you left only ", chance-1, "chance")
            chance -= 1

