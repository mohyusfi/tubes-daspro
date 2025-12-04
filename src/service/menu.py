def menu_utama():   
    while True: 
        print("====MENU UTAMA====")
        print("1. Mulai")
        print("2. Tambah Saldo")
        print("3. Tarik Saldo")
        print("4. Berhenti")
        menu = input("pilih menu: ")
        match menu:
            case "1":
                print("Mulai")
            case "2":
                print("Mulai")
            case "3":
                print("Mulai")
            case "4":
                break
            case _:
                print("menu tidak di temukan!")
        
if __name__ == "__main__":
    menu_utama()

