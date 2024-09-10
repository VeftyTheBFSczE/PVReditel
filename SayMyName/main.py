while True:
    print("Hello whats your name buddy?")
    name = input()
    print(f"Is your name {name}?")
    answer = input()
    if answer == "yes":
        print(f"Thank you {name} and have a nice day")
        break
    else:
        print("You lied to me, I feel betrayed.")
