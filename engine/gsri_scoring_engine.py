import random

class GSRIScoringEngine:
    def __init__(self, threshold=40.0):
        self.threshold = threshold
        self.current_score = 25.0 # Baseline

    def calculate_score(self, telemetry_data):
        # Logic to derive G-SRI from multidimensional telemetry
        volatility = random.uniform(0.8, 1.2)
        self.current_score = (self.current_score * volatility) + random.uniform(-1, 1.5)
        return round(self.current_score, 2)

    def is_safe(self):
        return self.current_score < self.threshold

if __name__ == "__main__":
    engine = GSRIScoringEngine()
    score = engine.calculate_score({})
    print(f"Current G-SRI: {score} (Safe: {engine.is_safe()})")
