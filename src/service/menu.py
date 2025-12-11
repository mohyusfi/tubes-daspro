from service import judol_service as JudolService, wallet_service as WalletService
from utils import menu as UtilsMenu

def mainMenu():   
    while True: 
        UtilsMenu.userProfile()
        UtilsMenu.showListMenu()
        menu = input("pilih menu: ")
        match menu:
            case "1":
                try:
                    UtilsMenu.showLevel()   
                    level = int(input("level: "))
                    amount_bet = int(input("Jumlah taruhan: Rp."))
                    JudolService.playGame(amount_bet, level)
                except:
                    print("Terjadi Kesalahan!")
            case "2":
                try:
                    amount = int(input("Rp"))
                    WalletService.topupBalance(amount)
                    print(f"Berhasil menambah saldo: Rp{amount}")
                except:
                    print("Terjadi kesalahan")
            case "3":
                try:
                    bank = input("Bank: ")
                    accountNumber = input("Account Number: ")
                    amount = int(input("Rp"))
                    WalletService.withdrawBalance(bank, accountNumber, amount)
                except:
                    print("Terjadi kesalahan")
            case "4":
                break
            case _:
                print("menu tidak di temukan!")
        
        print("\n\n")

if __name__ == "__main__":
    mainMenu()