import random

def check_soil_moisture():
    # Simulate soil moisture levels (range: 0 to 100)
    moisture_level = random.randint(0, 100)
    return moisture_level

def take_action(moisture_level, threshold=30):
    if moisture_level < threshold:
        print(f"Alert: Soil moisture level is {moisture_level}%. Take action!")

if __name__ == "__main__":
    # Check soil moisture
    current_moisture = check_soil_moisture()

    # Display current moisture level
    print(f"Current Soil Moisture Level: {current_moisture}%")

    # Check if action is needed
    take_action(current_moisture)
