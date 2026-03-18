# Create a dictionary of electrical components
components = {
    'R1': ('Resistor', 1000, '5%'),
    'R2': ('Resistor', 2200, '10%'),
    'C1': ('Capacitor', 1e-6, '20%'),
    'C3': ('Capacitor', 1e-7, '5%')
}

# Print the initial dictionary
print("Initial dictionary:")
print(components)
print()

# Update the tolerance of C3 to 10%
components['C3'] = ('Capacitor', 1e-7, '10%')

# Add C2 with capacitance of 2.2e-6 and tolerance of 15%
components['C2'] = ('Capacitor', 2.2e-6, '15%')

# Print the updated dictionary
print("Updated dictionary:")
print(components)
