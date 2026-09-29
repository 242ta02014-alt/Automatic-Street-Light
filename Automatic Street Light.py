# Automatic Street Light
# Easy Python Code

light = int(input("Enter light intensity (0-100): "))

print("\n--- AUTOMATIC STREET LIGHT ---")

if light < 40:
    print("It is DARK")
    print("Street Light: ON")

else:
    print("It is BRIGHT")
    print("Street Light: OFF")
