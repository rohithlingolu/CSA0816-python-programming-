denominations = [2000, 500, 200, 100]
total_balance = 0

for i in range(4):
    denomination = int(input(f"Enter the {i+1} Denomination: "))
    notes = int(input(f"Enter the {i+1} Denomination number of notes: "))
    total_balance += denomination * notes

print("\nTotal Available Balance in ATM:", total_balance)
