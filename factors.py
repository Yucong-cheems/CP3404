def find_factors(number):
    factors = set()
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return factors

distances = [18, 30, 24]
all_factors = {}

for distance in distances:
    all_factors[distance] = find_factors(distance)

for distance, factors in all_factors.items():
    print(f"Distance: {distance}, Factors: {sorted(factors)}")

