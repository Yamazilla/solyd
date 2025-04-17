with open("lista.txt", "r") as file:
    for line in file:
        print(f"item: {line.strip()}")