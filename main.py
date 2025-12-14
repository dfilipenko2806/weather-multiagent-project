from orchestrator import run

if __name__ == "__main__":
    city = input("Введите город: ")
    preferences = input("Есть ли пищевые предпочтения? (например: не люблю помидоры): ")

    result = run(city, preferences)

    for key, value in result.items():
        print(f"\n=== {key.upper()} ===")
        print(value)
