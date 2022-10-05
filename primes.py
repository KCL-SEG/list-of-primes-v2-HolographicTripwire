"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

prime_numbers = [2,3]

# Return a list containing a number of primes equal to n
def primes(number_of_primes):
    # Throw an error when given invalid inputs
    if(number_of_primes <= 0):
        raise ValueError("The number of requested primes must be greater zero")
    # Create a list
    list = []
    # Add a number of primes to the list equal to the number requested
    for prime in range(number_of_primes):
        list.append(get_prime(prime))
    # Return the list
    return list

# Get the nth prime
def get_prime(n):
    # Calculate if any new primes need to be created to reach n
    new_primes = n-len(prime_numbers)+1
    # Create a number of new primes equal to the number calculated
    for i in range(new_primes):
        create_prime()
    # Return the nth prime
    return prime_numbers[n]

# Add one new prime to the list of primes
def create_prime():
    # Find the current largest prime
    largest = prime_numbers[len(prime_numbers) - 1] + 2
    print(largest)
    # Keep incrementing until a prime number is found
    while not is_prime(largest):
        print(largest)
        largest += 2
    # Add the new prime to the list
    prime_numbers.append(largest)

# Check if a number is divisible by any of the currently stored primes
# Note that this should only be called in by create_prime()
def is_prime(num):
    # Iterate through all current primes
    for prime in prime_numbers:
        # Break if you reach 50% of the number, as no factors are over 50%
        if prime > (num/2):
            break
        # Return false if the number is divisible by another prime
        if num / prime == int(num / prime):
            return False
    # Return true if the number was not divisible by ANY primes
    return True
