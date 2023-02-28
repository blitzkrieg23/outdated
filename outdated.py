from datetime import datetime

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date_str = input("Please enter a date : ").strip()
    try:
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
    except ValueError:
        try:
            date_obj = datetime.strptime(date_str, '%B %d, %Y')
        except ValueError:
            print("Invalid date format. Please try again.")
            continue

    if date_obj.year < 1:
        print("Invalid year. Please try again.")
        continue

    date_str = date_obj.strftime('%Y-%m-%d')
    print(date_str)
    break
