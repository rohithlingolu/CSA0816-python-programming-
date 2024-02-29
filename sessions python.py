def find_season(month, day):
    if (month == "Mar" and day >= 20) or (month == "Apr") or (month == "May") or (month == "Jun" and day < 21):
        return "Spring"
    elif (month == "Jun" and day >= 21) or (month == "Jul") or (month == "Aug") or (month == "Sep" and day < 22):
        return "Summer"
    elif (month == "Sep" and day >= 22) or (month == "Oct") or (month == "Nov") or (month == "Dec" and day < 21):
        return "Fall"
    else:
        return "Winter"

def main():
    month = input("Enter the month: ").capitalize()[:3]
    day = int(input("Enter the date: "))

    season = find_season(month, day)
    print(f"The season is currently {season}")

if __name__ == "__main__":
    main()
