import random
import pandas as pd
import numpy as np
import math

# Taking input
student_name = input("Enter your name: ")
roll_number = int(input("Enter your roll number: "))
num_zones = int(input("Enter number of zones (15-20 recommended): "))

print("\nChoose Priority:")
print("1. Air Quality")
print("2. Traffic")
print("3. Energy")

choice = int(input("Enter choice (1/2/3): "))

if choice == 1:
    priority = "Air Quality"
elif choice == 2:
    priority = "Traffic"
else:
    priority = "Energy"


# Generate data
zones = []
for i in range(num_zones):
    zone_data = {
        "zone": i + 1,
        "traffic": random.randint(0, 100),
        "air_quality": random.randint(0, 300),
        "energy": random.randint(0, 500)
    }
    zones.append(zone_data)

# Add some extreme values
if num_zones >= 3:
    zones[0]["traffic"] = 0
    zones[1]["air_quality"] = 290
    zones[2]["energy"] = 480


# Classification
def classify_zone(r):
    if r["air_quality"] > 200 or r["traffic"] > 80:
        return "High Risk"
    elif r["energy"] > 400:
        return "Energy Critical"
    elif r["traffic"] < 30 and r["air_quality"] < 100:
        return "Safe Zone"
    else:
        return "Moderate"


# Risk score calculation
def calculate_risk_score(r):
    if priority == "Air Quality":
        w_t, w_a, w_e = 0.2, 0.6, 0.2
    elif priority == "Traffic":
        w_t, w_a, w_e = 0.5, 0.3, 0.2
    else:
        w_t, w_a, w_e = 0.2, 0.3, 0.5

    score = r["traffic"] * w_t + r["air_quality"] * w_a + r["energy"] * w_e
    return score


# Sorting based on priority
if priority == "Air Quality":
    zones = sorted(zones, key=lambda x: x["air_quality"])
    strategy = "Best Air Quality First"
elif priority == "Traffic":
    zones = sorted(zones, key=lambda x: x["traffic"])
    strategy = "Low Traffic First"
else:
    zones = sorted(zones, key=lambda x: x["energy"])
    strategy = "Low Energy Usage First"


# Shuffle for variation
if roll_number % 3 == 0:
    random.shuffle(zones)


# Add category and risk score
for r in zones:
    r["category"] = classify_zone(r)
    r["risk_score"] = calculate_risk_score(r)


# Convert to DataFrame
df = pd.DataFrame(zones)

# Mean values
mean_values = df[["traffic", "air_quality", "energy"]].mean()

# Top 3 risky zones
top3 = df.sort_values(by="risk_score", ascending=False).head(3)

# Pattern detection
threshold = df["risk_score"].mean()
high_risk = df[df["risk_score"] > threshold]

variance = np.var(df["traffic"])
if variance < 800:
    stability = "Stable"
else:
    stability = "Unstable"

clusters = high_risk["zone"].tolist()

# Risk stats
max_risk = df["risk_score"].max()
avg_risk = df["risk_score"].mean()
min_risk = df["risk_score"].min()

# Final decision
if avg_risk < 50:
    decision = "City Stable"
elif avg_risk < 120:
    decision = "Moderate Risk"
elif avg_risk < 200:
    decision = "High Alert"
else:
    decision = "Critical Emergency"


# Output
print(f"\n--- Smart City Report by {student_name} ---")
print("Priority:", priority)
print("Zones:", num_zones)

print("\nData:\n", df)

print("\nMean Values:\n", mean_values)

print("\nTop 3 Risk Zones:\n", top3)

print("\nRisk Stats:", (max_risk, avg_risk, min_risk))
print("Stability:", stability)
print("High Risk Zones:", clusters)

print("\nStrategy:", strategy)
print("Final Decision:", decision)

print("\nInsight:")
print("Smart city systems help in managing resources efficiently based on data.")
