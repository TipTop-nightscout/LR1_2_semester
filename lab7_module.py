def menu(cyber_threats):
    print("\nЛР 7")

    while True:
        print("\nMENU (ЛР 7)")
        print("1. Search by threat name")
        print("2. Search by keyword")
        print("3. Add/Update threat")
        print("4. Delete threat")
        print("5. Show all")
        print("6. Exit to Main Menu")

        choice = input("Choice: ").strip()

        if choice == '1':
            name = input("Name: ")
            desc = cyber_threats.get(name)
            print(f"Found: {desc}" if desc else "Not found.")
        elif choice == '2':
            key = input("Keyword: ")
            found = [t for t, d in cyber_threats.items() if key.lower() in d.lower()]
            print(f"Found: {found}" if found else "None found.")
        elif choice == '3':
            name = input("Name: ")
            cyber_threats[name] = input("Description: ")
            print("Saved.")
        elif choice == '4':
            if cyber_threats.pop(input("Name to delete: "), None):
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == '5':
            for t, d in cyber_threats.items(): print(f"[{t}]: {d}")
        elif choice == '6':
            break