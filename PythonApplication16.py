import random
def bank_deposit():
    initial_amount = float(input("Enter the initial deposit amount: "))
    interest_rate = float(input("Enter the annual interest rate (in percentage): ")) / 100
    desired_amount = float(input("Enter the desired final amount: "))

    year = 0
    current_amount = initial_amount

    print("\nAmount in the deposit over the years:")
    while current_amount < desired_amount:
        current_amount += current_amount * interest_rate
        year += 1
        print(f"Year {year}: {current_amount:.2f}")

    print(f"\nThe deposit will reach or exceed the desired amount in {year} years.")

def guess_the_number_game():
    secret_number = random.randint(1, 100)
    attempts = 7

    print("Guess the Number Game!")
    print("I've chosen a number between 1 and 100. You have 7 attempts.")

    for attempt in range(1, attempts + 1):
        try:
            user_guess = int(input(f"Attempt {attempt}: Enter your guess: "))
            if user_guess < secret_number:
                print("The secret number is higher.")
            elif user_guess > secret_number:
                print("The secret number is lower.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
                break
        except ValueError:
            print("Please enter an integer.")
    else:
        print(f"\nYou've used all {attempts} attempts. The secret number was {secret_number}.")
def find_prime_numbers():
    while True:
        try:
            lower_bound = int(input("Enter the lower bound of the range: "))
            upper_bound = int(input("Enter the upper bound of the range: "))
            if lower_bound >= upper_bound:
                print("The lower bound must be less than the upper bound.")
            elif lower_bound < 2 and upper_bound < 2:
                print("There are no prime numbers in the specified range.")
                return
            break
        except ValueError:
            print("Please enter integers.")

    prime_numbers = []
    for number in range(lower_bound, upper_bound + 1):
        if number > 1:
            is_prime = True
            for divisor in range(2, int(number**0.5) + 1):
                if number % divisor == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(number)

    if prime_numbers:
        print("Prime numbers in the specified range:")
        print(prime_numbers)
    else:
        print("There are no prime numbers in the specified range.")
def calculate_factorial():
    while True:
        try:
            number = int(input("Enter a non-negative integer to calculate its factorial: "))
            if number < 0:
                print("Please enter a non-negative number.")
            else:
                break
        except ValueError:
            print("Please enter an integer.")

    factorial = 1
    multiplication_steps = "1"
    i = 2
    while i <= number:
        factorial *= i
        multiplication_steps += f"*{i}"
        i += 1

    print(f"{number}! = {multiplication_steps} = {factorial}")
def model_bacterial_growth():
    initial_population = 10
    growth_rate = 0.20  # 20%
    max_population = 0

    while max_population <= initial_population:
        try:
            max_population = int(input("Enter the maximum population of bacteria: "))
            if max_population <= initial_population:
                print("The maximum population must be greater than the initial population.")
            else:
                break
        except ValueError:
            print("Please enter an integer.")

    current_population = initial_population
    hours = 0

    print("\nBacterial population growth over hours:")
    while current_population < max_population:
        print(f"Hour {hours}: {int(current_population)}")
        current_population *= (1 + growth_rate)
        hours += 1

    print(f"Hour {hours}: {int(current_population)}")
    print(f"\nThe population will reach or exceed {max_population} bacteria in {hours} hours.")

bank_deposit()
guess_the_number_game()
find_prime_numbers()
calculate_factorial()
model_bacterial_growth()