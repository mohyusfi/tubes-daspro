from service import wallet_service as WalletService

def showListMenu():
    print("====MENU UTAMA====")
    print("1. Mulai")
    print("2. Tambah Saldo")
    print("3. Tarik Saldo")
    print("4. Berhenti")


def showLevel():
    print("====LEVEL====")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

def userProfile():
    print("\n\n")
    print(f"SALDO ANDA: {WalletService.balance}")