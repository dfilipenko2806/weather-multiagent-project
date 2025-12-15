from orchestrator import run

city = input("Enter your city: ")
food_preferences = input("Any food preferences? (e.g., dislike tomatoes): ")

print("\nPlanning your evening...\n")

result = run(city, food_preferences)

print("=== WEATHER ===")
print(result["weather"])

print("\n=== ACTIVITY ===")
for i, act in enumerate(result["activity"], 1):
    print(f"{i}. {act}")

print("\n=== FOOD ===")
for i, f in enumerate(result["food"], 1):
    print(f"{i}. {f}")

print("\n=== LOCATION ===")
for i, loc in enumerate(result["location"], 1):
    print(f"{i}. {loc}")

print("\n=== OUTFIT ===")
for i, item in enumerate(result["outfit"], 1):
    print(f"{i}. {item}")
