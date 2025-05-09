# Prime Number Finder Program

def is_prime(num):
    # Check if the number is prime
    if num < 2:
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # Not a prime number if divisible by any number in range
    return True

def find_primes(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")

def main():
    # Input interval from user
    start = int(input("Enter the starting number of the interval: "))
    end = int(input("Enter the ending number of the interval: "))
    
    # Call function to find and display prime numbers
    find_primes(start, end)

# Run the program
if __name__ == "__main__":
    main()
