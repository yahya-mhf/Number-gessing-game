def rand(low = 1, hight = 100):
    from datetime import datetime

    now = datetime.now()

    time_int = int(now.strftime("%Y%m%d%H%M%S%f"))

    return low + time_int % (hight - low + 1)

def main():
    while True:
        r = rand()
        try:
            d = int(input("""
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
Enter your choice: """))

        except ValueError:
            print("\nPlease enter a valid choice")
            continue
        except KeyboardInterrupt:
            print("\nExiting program. Goodbye!")
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
                print(f"    Congratulations! You guessed the correct number in {i + 1} attempts.")
                win = True
                break
        if win:
            continue
        else:
            print(f"   You Failed !? the correct number is {r}")


if __name__=="__main__":
    main()

# To-DO
# make the limit numbers chosed by user by custimizing that with number of attempts
# add the feature that the user challenge the engine
# make a GUI
