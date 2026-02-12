import re

N = 0
A = []
B = []


def lab5_task1_input_globals():
    global N, A, B
    print("\nЛР 5. Task 1")
    N = int(input("Enter N: "))
    A = []
    B = []

    i = 0
    while i < N:
        ai = float(input(f"A[{i + 1}]: ").strip())
        bi = float(input(f"B[{i + 1}]: ").strip())
        A.append(ai)
        B.append(bi)
        i += 1


def lab5_task1_process_globals():
    global N, A, B

    if N == 0:
        print("Enter N first.")
        return

    i = 0
    Sa = 0.0
    Sb = 0.0

    while i < N:
        Sa += A[i]
        Sb += B[i]
        i += 1

    Sa = Sa / N
    Sb = Sb / N

    i = 0
    K1 = 0
    K2 = 0

    while i < N:
        c = A[i] - Sa
        d = B[i] - Sb
        if c > 0 and d > 0:
            K1 = K1 + 1
        elif c < 0 and d < 0:
            K2 = K2 + 1
        i = i + 1

    K = (K1 + K2) / N

    print(f"N={N}")
    print(f"mean(A)={Sa:.6f}, mean(B)={Sb:.6f}")
    print(f"K1={K1}, K2={K2}, K={K:.6f}")

    if K > 0.5:
        print("Relations between series A and series B is real")
    else:
        print("Relations between series A and series B is not real")

def lab5_task2_output(regions, years, crime_data):
    print("\nЛР 5. Task 2")
    print("Data about crimes:")
    for name, row in zip(regions, crime_data):
        print(f"{name}: {row}")

    totals = [sum(col) for col in zip(*crime_data)]
    print("а) Total number of crimes per year:")
    for year, total in zip(years, totals):
        print(f" **{year}**: {total}")

    print("b) The year with the highest number of crimes in each region:")
    for name, row in zip(regions, crime_data):
        max_year = years[row.index(max(row))]
        print(f" **{name}**: {max_year}")

def lab6(text):
    print("\nЛР 6")
    text_lower = text.lower()
    words = re.findall(r"[a-zA-Zа-яА-ЯёЁіІїЇєЄ]+", text_lower)

    matching = [w for w in words if len(w) > 1 and w[0] == w[-1]]

    if matching:
        print("Words that begin and end with the same letter:")
        for j in matching:
            print(j)
    else:
        print("These words were not found")

def lab7_menu(cyber_threats):
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

if __name__ == "__main__":
    while True:
        print("\nMain menu")
        print("1. ЛР 5.1")
        print("2. ЛР 5.2")
        print("3. ЛР 6")
        print("4. ЛР 7")
        print("0. Exit")

        choice = input("Your choice: ")

        if choice == '1':
            lab5_task1_input_globals()
            lab5_task1_process_globals()

        elif choice == '2':
            regions = ["Kyiv", "Kharkiv", "Poltava", "Chernihiv", "Sumy", "Donetsk"]
            years = [2006, 2007, 2008, 2009, 2010]
            data = [
                [1699, 1695, 1276, 1562, 1853],
                [1324, 1470, 1337, 1758, 1038],
                [1343, 1562, 1939, 1865, 1415],
                [1984, 1303, 1964, 1516, 1723],
                [1035, 1622, 1058, 1786, 1472],
                [1706, 1538, 2141, 2921, 1803]
            ]
            lab5_task2_output(regions, years, data)

        elif choice == '3':
            text = input("Enter text: ").strip()
            lab6(text)

        elif choice == '4':
            threats = {
                "Phishing": "Fraud aiming to gain access to data.",
                "Ransomware": "Extortion software.",
                "Malware": "Malicious software.",
                "DDoS": "Denial of service attack."
            }
            lab7_menu(threats)

        elif choice == '0':
            print("Exit.")
            break
