
total_minutes = int(input("Enter the total number of minutes: "))       # Input: total number of minutes

hours = total_minutes // 60             # Convert minutes into hours and remaining minutes
minutes = total_minutes % 60

print(f"{total_minutes} minutes is equal to {hours} hour(s) and {minutes} minute(s).")
