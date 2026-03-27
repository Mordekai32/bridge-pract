def check_day(day):
    if day == "Monday":
        return "Start of the work week"
    elif day == "Friday":
        return "Almost weekend!"
    elif day in ["Saturday", "Sunday"]:
        return "Weekend!"
    else:
        return "Just another day"

print(check_day("Friday"))