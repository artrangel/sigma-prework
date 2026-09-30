list_no = []  # Empty initial list for the integer array
action = ""
while action != "yes":
    integer = int(input("Input an integer: "))
    list_no.append(integer)
    action = input("Are you done? (yes or no): ")

# Initial values set
min = list_no[0]
max = list_no[0]

# Using a for loop to find the min and max values of the integer list
for n in range(len(list_no)):
    if list_no[n] < min:
        min = list_no[n]
    elif list_no[n] > max:
        max = list_no[n]

print([min, max])
