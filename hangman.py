import random
li = [' _____________________',
      '|                  |', '|                 (-)', '|               _/| |\_', '|               _/ - \_', '|', '|', '|======================']


def hangman():
    list_of_word = ["phone", "sun", "moon", "earth"]
    word = random.choice(list_of_word)
    ind = list_of_word.index(word)
    guess_made = []
    vaild_entery = set("abcdefghijklmnopqrstuvwxyz")
    H = ['I think its always in you pocket', 'biggest start in univers',
         'It is shining in the night', 'Inside the this you got 3/4 water only']
    x = 1
    count_r = 0
    d = {}
    for i in word:
        guess_made.append('_')
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    while x != len(li):
        print(f"{H[ind]}\n{guess_made}")
        guess = input("guess the charcter of the word__:")
        if guess not in d:
            for hs in range(x):
                print(li[hs])
            x += 1
        else:
            if d[guess] == 1:
                ind1 = word.index(guess)
                guess_made[ind1] = guess
                count_r += 1
            if d[guess] == 2:
                ind1 = word.index(guess)
                ind2 = word.index(guess, ind1+1)
                guess_made[ind2] = guess
                count_r += 1
            d[guess] -= 1
            if d[guess] == 0:
                d.pop(guess)
        if count_r == len(word):
            print(
                f'superb !!!!\nyou guess the correct!!!\n{H[ind]}\nthe word is >>>>@ {word}')
            break
    else:
        print('YOU LATE A DIE GOOD MAN\nyou are bad man ')


name = input('What is your name ____: ')
print(f'Welcome {name} And guess the word \nall the best')
hangman()
