from service import wallet_service as WalletService

def maskedNumber(value):
    strValue = str(value)
    return '*' * (len(strValue) - 4) + strValue[-4:]

def validateAmountBet(amountBet):
    if amountBet > WalletService.balance:
        raise ValueError("Saldo Tidak Cukup")

# testing
if __name__ == "__main__":
    print(maskedNumber(1231249329423940))