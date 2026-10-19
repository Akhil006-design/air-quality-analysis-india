# Internship Task 1: Python Basics

# 1. Variables and data types
city = "Delhi"
aqi = 259.49

print("AIR QUALITY REPORT")
print("------------------")
print("City:", city)
print("Average AQI:", aqi)

# 2. Conditional statements
if aqi <= 50:
    category = "Good"
elif aqi <= 100:
    category = "Satisfactory"
elif aqi <= 200:
    category = "Moderate"
elif aqi <= 300:
    category = "Poor"
elif aqi <= 400:
    category = "Very Poor"
else:
    category = "Severe"

print("AQI Category:", category)

# 3. Lists and loops
cities = ["Delhi", "Patna", "Lucknow"]
aqi_values = [259.49, 240.78, 217.97]

print("\nCITY AQI COMPARISON")

for i in range(len(cities)):
    print(cities[i], ":", aqi_values[i])

# 4. Dictionary
city_aqi = {
    "Delhi": 259.49,
    "Patna": 240.78,
    "Lucknow": 217.97
}

print("\nDelhi AQI:", city_aqi["Delhi"])

# 5. Function
def check_aqi(value):
    if value <= 100:
        return "Relatively lower AQI"
    else:
        return "Higher AQI"

print("Delhi assessment:", check_aqi(aqi))

# 6. Average calculation
total = 0

for value in aqi_values:
    total = total + value

average_aqi = total / len(aqi_values)

print("\nAverage AQI:", round(average_aqi, 2))