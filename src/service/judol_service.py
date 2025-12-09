import random

def playLevel1(bet, balance):
    mathRandom = random.randrange(1, 4, 1)
    userBalance = balance

    print("ACHIEVE 3X RETURNS!")
    print("________________")
    print("| ❓ | ❓ | ❓ |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    userChoice = int(input("CHOOSE YOUR LUCKY BOX(1-3):"))
    match mathRandom:
        case 1:
            print("________________")
            print("| 🍒 | 💣 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 2:
            print("________________")
            print("| 💣 | 🍒 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 3:
            print("________________")
            print("| 💣 | 💣 | 🍒 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    userBalance = balance + 2*bet if userChoice == mathRandom else balance - bet
    print(f"YOUR CHOICE IS RIGHT!!\nYOUR BET Rp.{bet}\nYOU GOT Rp." + str(bet*3)) if userChoice == mathRandom else print("YOUR CHOICE IS WRONG!!")
    print("YOUR BALANCE:", userBalance)

def playLevel2(bet, balance):
    mathRandom = random.randrange(1, 5, 1)

    print("\nACHIEVE 5X RETURNS!")
    print("___________________")
    print("| ❓ | ❓ | ❓ | ❓ |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    userChoice = int(input("CHOOSE YOUR LUCKY BOX(1-4):"))
    match mathRandom:
        case 1:
            print("______________________")
            print("| 🍒 | 💣 | 💣 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 2:
            print("______________________")
            print("| 💣 | 🍒 | 💣 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 3:
            print("______________________")
            print("| 💣 | 💣 | 🍒 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 4:
            print("______________________")
            print("| 💣 | 💣 | 💣 | 🍒 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    userBalance = balance + 4*bet if userChoice == mathRandom else balance - bet
    print(f"YOUR CHOICE IS RIGHT!!\nYOUR BET Rp.{bet}\nYOU GOT Rp." + str(bet*5)) if userChoice == mathRandom else print("YOUR CHOICE IS WRONG!!")
    print("YOUR BALANCE:", userBalance)

def playLevel3(bet, balance):
    mathRandom = random.randrange(1, 6, 1)

    print("\nACHIEVE 10X RETURNS!")
    print("________________________")
    print("| ❓ | ❓ | ❓ | ❓ | ❓ |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    userChoice = int(input("CHOOSE YOUR LUCKY BOX(1-5):"))
    match mathRandom:
        case 1:
            print("____________________________")
            print("| 🍒 | 💣 | 💣 | 💣 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 2:
            print("____________________________")
            print("| 💣 | 🍒 | 💣 | 💣 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 3:
            print("____________________________")
            print("| 💣 | 💣 | 🍒 | 💣 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 4:
            print("____________________________")
            print("| 💣 | 💣 | 💣 | 🍒 | 💣 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        case 5:
            print("____________________________")
            print("| 💣 | 💣 | 💣 | 💣 | 🍒 |")
            print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

    userBalance = balance + 9*bet if userChoice == mathRandom else balance - bet
    print(f"YOUR CHOICE IS RIGHT!!\nYOUR BET Rp.{bet}\nYOU GOT Rp." + str(bet*10)) if userChoice == mathRandom else print("YOUR CHOICE IS WRONG!!")
    print("YOUR BALANCE:", userBalance)

    return userBalance

def playGame(bet, level, balance):
    match level:
        case 1:
            playLevel1(bet, balance)
        case 2:
            playLevel2(bet, balance)
        case 3:
            playLevel3(bet, balance)


