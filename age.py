from datetime import datetime  # imports date
present = datetime.now()  # to obtain today's date and time

date_given = input(
    "Please input a given date you want to calculate for age: (DD-MM-YYYY): ")
date_format = datetime.strptime(
    date_given, "%d-%m-%Y")  # Format in proper date


# In the case of the birthday still hasn't passed yet
if (date_format.month, date_format.day) > (present.month, present.day):
    age = (present.year-date_format.year)-1
else:
    age = present.year-date_format.year
print(f"Current age is: {age}")  # Prints out the age
