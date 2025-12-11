from utils import balance as BalanceUtils

balance = 0

def topupBalance(amount):
    try:
        global balance
        validated = int(amount)
        balance += validated
    except:
        print("terjadi kesalahan!!")

def decreaseBalance(amount):
    try:
        global balance
        validated = int(amount)
        balance -= validated
    except:
        print("Terjadi Kesalahan!!")

def withdrawBalance(bank, accountNumber, amount):
    try:
        global balance
        validatedAmount = int(amount)
        accountNumber = int(accountNumber)
        if balance < validatedAmount:
            raise ValueError(f"Saldo anda kurang dari {validatedAmount}")
        balance -= validatedAmount
        print(f"Berhasil tarik uang sejumlah Rp{validatedAmount}")
        print(f"BANK: {bank}, ACC_NUMBER: {BalanceUtils.maskedNumber(accountNumber)}")
    except Exception as e:
        print(f"{e}")
        

# testing
if __name__ == "__main__":
    topupBalance(10000)
    decreaseBalance(1000)
    withdrawBalance("BCA", 1231432423423, 8_000)
    print(balance)


    