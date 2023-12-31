import random

class Greenhouse:
    def __init__(self, target_temperature=25):
        self.current_temperature = random.uniform(20, 30)  # Simulate initial temperature
        self.target_temperature = target_temperature

    def measure_temperature(self):
        # Simulate temperature fluctuation (adjust as needed)
        temperature_change = random.uniform(-1, 1)
        self.current_temperature += temperature_change

    def adjust_cooling_system(self):
        if self.current_temperature > self.target_temperature + 1:
            print("Turning on the cooling system.")
        elif self.current_temperature < self.target_temperature - 1:
            print("Turning off the cooling system.")

if __name__ == "__main__":
    # Create a greenhouse instance with a target temperature of 25 degrees Celsius
    greenhouse = Greenhouse(target_temperature=25)

    # Simulate monitoring and adjusting the greenhouse conditions
    for _ in range(10):
        greenhouse.measure_temperature()
        print(f"Current Temperature: {greenhouse.current_temperature:.2f}\u00b0C")

        greenhouse.adjust_cooling_system()
