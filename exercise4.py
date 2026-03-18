import random

# Create an empty list called stack
stack = []

def push(x):
    """Push a value onto the stack."""
    stack.append(x)

def pop():
    """Pop and return a value from the stack."""
    return stack.pop()

# Seed the random number generator with 123
random.seed(123)

# Push 5 random numbers and print them
print("Pushing random numbers:")
for i in range(5):
    random_num = random.random()
    push(random_num)
    print(f"Pushed: {random_num}")

print("\nPopping values from stack:")
# While the stack is not empty, pop values and print them
while stack:
    value = pop()
    print(f"Popped: {value}")
