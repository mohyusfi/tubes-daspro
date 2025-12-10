from service import judol_service as JudolService
from utils import menu as UtilsMenu

def mainMenu():   
    while True: 
        UtilsMenu.showListMenu()
        menu = input("pilih menu: ")
        match menu:
            case "1":
                try:
                    UtilsMenu.showLevel()   
                    level = int(input("level: "))
                    amount_bet = int(input("Jumlah taruhan: Rp."))
                    JudolService.playGame(amount_bet, level, 10000)
                except:
                    print("Terjadi Kesalahan!")
            case "2":
                print("Mulai")
            case "3":
                print("Mulai")
            case "4":
                break
            case _:
                print("menu tidak di temukan!")
        
        print("\n\n\n")

if __name__ == "__main__":
    mainMenu()