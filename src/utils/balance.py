def maskedNumber(value):
    strValue = str(value)
    return '*' * (len(strValue) - 4) + strValue[-4:]


# testing
if __name__ == "__main__":
    print(maskedNumber(1231249329423940))