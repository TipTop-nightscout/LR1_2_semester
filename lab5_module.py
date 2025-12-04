N = 0
A = []
B = []


def task1_input_globals():
    global N, A, B
    print("\nЛР 5. Завдання 1")
    try:
        N_input = int(input("Enter N: "))
        A_temp = []
        B_temp = []

        i = 0
        while i < N_input:
            ai = float(input(f"A[{i + 1}]: ").strip())
            bi = float(input(f"B[{i + 1}]: ").strip())
            A_temp.append(ai)
            B_temp.append(bi)
            i += 1

        N = N_input
        A = A_temp
        B = B_temp

    except ValueError:
        print("Помилка введення даних.")


def task1_process_globals():
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


def task2_process(regions, years, crime_data):
    print("\nЛР 5. Завдання 2")
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