import os

def rand(low = 1, hight = 100):
    from datetime import datetime

    now = datetime.now()

    time_int = int(now.strftime("%Y%m%d%H%M%S%f"))

    return low + time_int % (hight - low + 1)

def homescrean(ind = False):
    print("""
───────────────────────────────────
 🎮  Choose Your Difficulty Level  🎮
───────────────────────────────────
  1️⃣  Easy    (10 attempts)
  2️⃣  Medium  (5 attempts)
  3️⃣  Hard    (3 attempts)

 🔹 Press any other number for Default (Easy)
 🔹 To exit, press CTRL + C

 ⚠️  Warning: This game is just for coding practice!, Don't waste your Your time on it
 ⚠️  Don't waste your Your precious time ⚠️
───────────────────────────────────
""")
    if ind:
        print("Please enter a valid choice ⚠️\n")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') #Clear the terminal
        r = rand()

        d = 1
        ind = False
        c_stop = False
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') #Clear the terminal
            homescrean(ind)
            try:
                d = int(input("Enter your choice: "))
            except ValueError:
                ind = True
                continue
            except KeyboardInterrupt:
                print("\nExiting program. Goodbye!")
                c_stop = True
            break
        if c_stop:
            exit()

        n = 5 if d == 2 else (3 if d == 3 else 10)

        i = 0
        win = False
        while i < n:
            try:
                gess = int(input("Gess ? : "))
            except ValueError:
                print("Please enter a valid number")
                continue
            except KeyboardInterrupt:
                print("\nExiting program. Goodbye!")
                exit()
            if gess > r:
                print(f"    Incorrect! The number is less than {gess}")
                i += 1
            elif gess < r:
                print(f"    Incorrect! The number is greater than {gess}")
                i += 1
            else:
                win = True
                print(f"    ✅✅ Congratulations! You guessed the correct number in {i + 1} attempts. ✅✅")
                break
        if not win:
            print(f"\n  ❌❌  You Failed !? the correct number is {r} ❌❌")

        play_again = input("\nPlay again ❓ (y/n) ").lower()
        if play_again in ['y', 'yes']:
            continue
        break




if __name__=="__main__":
    main()

# To-DO
# make the limit numbers chosed by user by custimizing that with number of attempts
# add the feature that the user challenge the engine
# make a GUI
