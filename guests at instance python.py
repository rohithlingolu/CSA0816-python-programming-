def max_guests_at_any_instance(T, E, L):
    events = [(e, 1) for e in E] + [(l, -1) for l in L]
    events.sort()

    max_guests = 0
    current_guests = 0

    for event, change in events:
        current_guests += change
        max_guests = max(max_guests, current_guests)

    return max_guests

def main():
    test_cases = [
        (-4, [1, 5, 9, 10], [0, 2, 3, 4]),
        (0, [10, 2, 3, 4], [1234]),
        (4, [12, 85], [100]),
        (5, [42, 0, 35, 12, 15], [1, 2, 1, 3, 4]),
        (1, [12], [10])
    ]

    for T, E, L in test_cases:
        result = max_guests_at_any_instance(T, E, L)
        print(f"T={T}, E={E}, L={L} -> Maximum number of guests: {result}")

if __name__ == "__main__":
    main()
