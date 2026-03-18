class Capacitor:
    """A class to represent a capacitor with capacitance property and energy calculation."""
    
    def __init__(self, capacitance):
        """Initialize the capacitor with a given capacitance in Farads."""
        self.capacitance = capacitance
    
    def energy(self, voltage):
        """
        Compute the energy stored in the capacitor given the voltage across it.
        Formula: E = C * V^2 / 2
        
        Args:
            voltage: The voltage across the capacitor in Volts
            
        Returns:
            The energy stored in Joules
        """
        return self.capacitance * voltage**2 / 2


# Create two capacitor objects
C1 = Capacitor(1.0e-6)  # C1 is a 1 μF capacitor
C2 = Capacitor(2.2e-6)  # C2 is a 2.2 μF capacitor

# Calculate and print the energy stored in each capacitor at 170V
voltage = 170

print(f"Energy stored in C1 (1.0 μF) at {voltage}V: {C1.energy(voltage):.6f} J")
print(f"Energy stored in C2 (2.2 μF) at {voltage}V: {C2.energy(voltage):.6f} J")
