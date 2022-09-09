
import random

questions = [':The International Literacy Day is observed on ?',
             ': The language of Lakshadweep. a Union Territory of India, is ?',
             ':In which group of places the Kumbha Mela is held every twelve years?',
             ':Bahubali festival is related to',
             ':Which day is observed as the World Standards  Day?',
             ':Which of the following was the theme of the World Red Cross and Red Crescent Day?',
             ':September 27 is celebrated every year as ?',
             ':Who is the author of Manas Ka-Hans ?',
             ':The death anniversary of which of the following leaders is observed as Martyrs Day ?',
             ':Who is the author of the epic Meghdoot"?']


options = [['Sep 8 ', 'Nov 28  ', 'May 2 ', 'Sep 22 '],
           ['1. Tamil', '2.Hindi', '3.Malayalam', '4.Telugu ', ' '],
           ['1.Ujjain.Purl.Prayag.Haridwar', '2.Prayag.Haridwar,Ujjain,Nasik     ',
               '3.Rameshwaram. Purl, Badrinath. Dwarika   ', '4.Chittakoot,Ujjain,Prayag,Haridwar', ' ', ' '],
           ['1.Islam ', '2.Hinduism     ', '3.Buddhism    ', '4.Jainism ', ' '],
           ['1,June 26 ', '2,Oct 14    ', '3,Nov 15    ', '4,Dec 2  ', ' '],
           ['1,Dignity for all-focus on women ', '2,Dignity for all-focus on Children',
               '3,Focus on health for all ', '4,Nourishment for all-focus on children ', ' '],
           ["1,Teachers' Day ", "2,National Integration Day  ",
               "3,World Tourism Day    ", "4,International Literacy Day  ", " "],
           [" 1,Khushwant Singh ", " 2,Prem Chand    ",
               " 3,Jayashankar Prasad    ", " 4,Amrit Lal Nagar   ", " "],
           ["1,Smt. Indira Gandhi  ", "2,PI. Jawaharlal Nehru  ",
               "3,Mahatma Gandhi  ", "4,Lal Bahadur Shastri   ", " "],
           ["1,Vishakadatta    ", "2,Valmiki    ", "3,Banabhatta    ", "4,Kalidas   ", "  "]]


helpline_options = [['1.Sep 8 ', '2.Nov 28 ', ], ['1.Telugu  ', '3.Malayalam'],
                    ['1.Ujjain.Purl.Prayag. Haridwar',
                        '2.Prayag.Haridwar,Ujjain,Nasik'],
                    ['4.Jainism ', '2,Hinduism'], ['1,June 26', '2,Oct 14'],
                    ['1,Dignity for all-focus on Children ',
                        '2.Dignity for all - focus on women'],
                    ["1,Teachers' Day  ", "3,World Tourism Day"],
                    ["4,Amrit Lal Nagar   ", "2,Khushwant Singh"], [
                        "1,Smt. Indira Gandhi  ", "3,Mahatma Gandhi"],
                    ["1,Banabhatta ", "4,Kalidas"]]

answers = [1, 3, 2, 4, 2, 2, 3, 4, 3, 4]
a_i = 0
amount = [1000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 9000]
win_a = 0

helpline = [') 50:50', ') phone call', ') skip', ') audience poll']


for i in range(len(questions)):
    print(questions[i])
    x = 1
    for j in options[i]:
        print("{0}.{1}".format(x, j))
        x += 1
    ans = int(input("press 5 for helpline\nchoose the correct answer___: "))
    if ans == answers[i]:
        print("you win !!!")
        win_a += amount[a_i]
        a_i += 1
    elif ans == 5:
        z = 1
        for h in helpline:
            print(f"{z}", h)
            z += 1
        h_ch = int(input("choose anyone __: "))
        if h_ch == 1:
            helpline.remove(') 50:50')
            for h_o in (helpline_options[i]):
                print(h_o)
            h_o_c = int(input("enter your answer____: "))
            if h_o_c == answers[i]:
                print("you win !!!")
                win_a += amount[a_i]
                a_i += 1
            else:
                print("you lose the game !!!")
                break
        if h_ch == 2:
            helpline.remove(') phone call')
            print("Whom you want to call\npress 1 for call mom\npress 2 for girlfriend")
            c_cho = int(input("choose anyone_____: "))
            if c_cho == 1:
                print("calling mom...........")
                print("mom says", answers[i])
                ans_m = int(input("submit you'r answer_____: "))
                if ans_m == answers[i]:
                    print("you win !!!")
                    win_a += amount[a_i]
                    a_i += 1
                else:
                    print("you lose the game !!!")
                    break
            if c_cho == 2:
                print("calling__girlfriend..........")
                print("girlfriend says ", answers[i])
                ans_g = int(input("submit you'r answer_____: "))
                if ans_g == answers[i]:
                    print("you win !!!")
                    win_a += amount[a_i]
                    a_i += 1
                else:
                    print("you lose the game !!!")
                    break
        if h_ch == 3:
            helpline.remove(") skip")
            continue
        if h_ch == 4:
            helpline.remove(') audience poll')
            print("according to audience poll")
            print(answers[i])
            a_p = int(input("enter answer____: "))
            if a_p == answers[i]:
                print("you win !!!")
                win_a += amount[a_i]
                a_i += 1
            else:
                print("you lose the game !!!")
                break
    else:
        print("you loose the game")
        break
print("your wining amount is ", win_a)
