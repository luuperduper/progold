import time

Price = "25"#For wheat
Mom = "Layla"
Backstory = f"""It was a dark night, Mia was about to buy some stocks for her mother, {Mom}
"""
Phillip = "Phillip is"

# Slow typing for Backstory
for char in Backstory:
    print(char, end='', flush=True)
    time.sleep(0.05)  # Adjust the delay (seconds) as needed

print()
time.sleep(1)

print("==Welcome to the story==")
time.sleep(1)
print()
time.sleep(1)

# Slow typing for the first line of dialogue
for char in "...Young girl walks into shop":
    print(char, end='', flush=True)
    time.sleep(0.1)

print()
time.sleep(1)

# Slow typing for the second line of dialogue
for char in "Mia: ...Hello, heard y'all take cash?":
    print(char, end='', flush=True)
    time.sleep(0.1)

print()
time.sleep(1)

# Slow typing for the third line of dialogue
for char in """\033[92mPhillip is a 30 year old man that has worked here since forever, never worked any other place\033[0m""":
    print(char, end='', flush=True)
    time.sleep(0.05)

print()
time.sleep(1)

# Slow typing for the fourth line of dialogue
for char in "Phillip:\033[1;31m Hell no! we only take gold round' here\033[0m":
    print(char, end='', flush=True)
    time.sleep(0.05)

print()
time.sleep(1)

# Slow typing for the fifth line of dialogue
for char in "Ive got gold, chill. Just tell me the prices":
    print(char, end='', flush=True)
    time.sleep(0.05)

print()
time.sleep(1)

def display_menu():
    print("Stock options")
    time.sleep(1)
    print("1. Tesla stock (525,000)")
    time.sleep(1)
    print("2. Walmart stock(615,000)")
    time.sleep(1)
    print("3. Coke stocks (100,000,000)")
    time.sleep(1)

def get_user_choice():
  while True:
    choice = input("Enter your choice (1-3): ")
    time.sleep(1)
    if choice.isdigit() and 1 <= int(choice) <= 3:
      return int(choice)
    else:
      print("Invalid choice. Please enter a number from 1-3.")
      time.sleep(1)

def process_choice(choice):
  """Processes the user's choice and shows the corresponding option."""
  if choice == 1:
    print("\033[92mYou chose Option 1! 550,000 gold spent.\033[0m")
    time.sleep(1)
  elif choice == 2:
    print("\033[92mYou chose Option 2! 600,000 gold spent.\033[0m")
    time.sleep(1)
  elif choice == 3:
    print("\033[92mYou chose Option 3! 700,000 gold spent.\033[0m")
    time.sleep(1)
# Main program loop
while True:
  display_menu()
  choice = get_user_choice()
  process_choice(choice)

  # Ask if the user wants to continue shopping
  continue_shopping = input("Do you want to continue shopping? (y/n): ").lower()
  time.sleep(1)

  if continue_shopping != 'y':
    print("Phillip: Thank you for shopping!")
    break