import random
import time

def generate_random_numbers():
    quantity = random.randint(100, 999)  # Generate a random three-digit quantity
    price = round(random.uniform(100, 999), 2)  # Generate a random three-digit price
    return quantity, price

def play_game():
    input("Press Enter to start timing...")  # Wait for user input to start timing
    start_time = time.time()

    quantity, price = generate_random_numbers()
    print(f"Random quantity: {quantity}")
    print(f"Random price: {price}")

    try:
        entered_quantity = int(input("Enter quantity (3 digits): "))
        entered_price = float(input("Enter price (3 digits): "))
    except ValueError:
        print("Invalid input. Please enter valid three-digit quantity and price.")
        return

    if not (100 <= entered_quantity <= 999) or not (100 <= entered_price <= 999):
        print("Quantity and price must be three-digit numbers.")
        return

    elapsed_time = time.time() - start_time
    print(f"Time taken to enter both quantity and price is {elapsed_time:.2f} seconds.")

    total_cost = entered_quantity * entered_price
    print(f"Total cost: {total_cost:.2f}")

    return elapsed_time

def main():
    total_time = 0
    num_games = 10

    for i in range(num_games):
        print(f"Game {i + 1}:")
        elapsed_time = play_game()
        total_time += elapsed_time
        print()

    average_time = total_time / num_games
    print(f"Average time across {num_games} games: {average_time:.2f} seconds")

if __name__ == "__main__":
    main()
