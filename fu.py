# Prime numbers using insert()

# Input range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# List to store primes
prime_list = []

# Function to check prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate primes
for num in range(start, end + 1):
    if is_prime(num):
        prime_list.append(num)  # normally add at the end

print("Primes using append:", prime_list)

# Now use insert to put 1 at the beginning
prime_list.insert(0, 1)
print("After insert at beginning:", prime_list)

# Use insert to put a number in the middle
middle_index = len(prime_list) // 2
prime_list.insert(middle_index, 99)
print("After insert in the middle:", prime_list)