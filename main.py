import lab5_module
import lab6_module
import lab7_module

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
            lab5_module.task1_input_globals()
            lab5_module.task1_process_globals()

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
            lab5_module.task2_process(regions, years, data)

        elif choice == '3':
            text_input = input("Enter text: ").strip()
            lab6_module.process_text(text_input)

        elif choice == '4':
            threats_dict = {
                "Phishing": "Fraud aiming to gain access to data.",
                "Ransomware": "Extortion software.",
                "Malware": "Malicious software.",
                "DDoS": "Denial of service attack."
            }
            lab7_module.menu(threats_dict)

        elif choice == '0':
            print("Exit.")
            break