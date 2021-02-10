print("BIRTHDAY CALCULATOR")
print("Current Day:")
current_m = int(input("Enter current month value (1-12): "))
current_d = int(input("Enter current day value (1-31): "))
current_y = int(input("Enter current year value: "))
print("Birthday:")
birth_m = int(input("Enter birth month value (1-12): "))
birth_d = int(input("Enter birth month value (1-31): "))
birth_y = int(input("Enter birth year value: "))
if (birth_m == current_m) and (birth_d == current_d):
    print("Happy Birthday!")
years_old = current_y - birth_y - 1
if(current_m==birth_m):
    if(current_d==birth_d):
        years_old = years_old + 1
if(current_m>birth_m):
    years_old = years_old + 1
print('You are ' + str(years_old) + ' years old.')
