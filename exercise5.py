import random

# Set up the loaded die probabilities
# Rolling a 6 is twice as likely as any other number
# P(1-5) = 1/7 each, P(6) = 2/7
outcomes = [1, 2, 3, 4, 5, 6]
weights = [1, 1, 1, 1, 1, 2]  # Weights corresponding to each outcome

# Number of simulated rolls
num_rolls = 100000

# Counter for rolls that sum to 8
count_eight = 0

# Run Monte Carlo simulation
for _ in range(num_rolls):
    # Roll two loaded dice
    die1 = random.choices(outcomes, weights=weights, k=1)[0] # random.choices returns one number in a list, we then take that element out of the list as an integer number and use that as the result of the die roll
    die2 = random.choices(outcomes, weights=weights, k=1)[0] # random.choices returns one number in a list, we then take that element out of the list as an integer number and use that as the result of the die roll

    # Check if sum equals 8
    if die1 + die2 == 8:
        count_eight += 1

# Calculate the estimated probability
estimated_probability = count_eight / num_rolls

print(f"Monte Carlo Simulation: Rolling Two Loaded Dice")
print(f"Number of simulations: {num_rolls}")
print(f"Number of rolls summing to 8: {count_eight}")
print(f"Estimated probability of rolling an 8: {estimated_probability:.6f}")
print(f"Estimated probability as a fraction: {count_eight}/{num_rolls}")
print(f"Theoretical probability: 1/7 ≈ {1/7:.6f}")
