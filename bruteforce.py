import itertools
import string
import time

def brute_force_crack(target_password, max_length):
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits  # You can add special characters if needed
    attempts = 0

    # Start timing
    start_time = time.time()

    # Iterate over all possible lengths
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            attempts += 1
            if guess_password == target_password:
                end_time = time.time()
                print(f"Password '{target_password}' cracked! It took {attempts} attempts and {end_time - start_time:.2f} seconds.")
                return guess_password

    print("Password not found within the given length.")
    return None

if __name__ == "__main__":
    target_password = input("Enter the password to crack: ")
    max_length = int(input("Enter the maximum length of the password: "))
    
    cracked_password = brute_force_crack(target_password, max_length)

    if cracked_password:
        print(f"Cracked password: {cracked_password}")
    else:
        print("Failed to crack the password.")
