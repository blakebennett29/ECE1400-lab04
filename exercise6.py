from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# Define the transfer function H(s) = s³ / (s³ + 2s² + 2s + 1)
numerator = [1, 0, 0, 0]      # s³ coefficients
denominator = [1, 2, 2, 1]    # s³ + 2s² + 2s + 1 coefficients

# Create transfer function
H = signal.TransferFunction(numerator, denominator)

# Define frequency range (0.01 Hz to 10 Hz)
# Use logarithmic spacing with at least 500 points (not equally spaced)
f = np.logspace(-2, 1, 500)  # 10^-2 to 10^1 Hz
omega = 2 * np.pi * f         # Convert to angular frequency (rad/s)

# Calculate frequency response
w, mag, phase = signal.bode(H, w=omega)

# Create the magnitude Bode plot
plt.semilogx(f, mag, 'b-', linewidth=2) #blue line for magnitude plot
plt.grid(True, which='both', alpha=0.3)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot')
plt.savefig('exercise6_bode_plot.png', dpi=150)
plt.show()

# Print summary information
print(f"Bode plot generated with {len(f)} points")
print(f"Frequency range: {f[0]:.4f} Hz to {f[-1]:.2f} Hz")
print(f"Magnitude range: {mag.min():.2f} dB to {mag.max():.2f} dB")
