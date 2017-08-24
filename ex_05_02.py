largest = None
smallest = None
while True:
    num_str = input("Enter a number: ")
    if num_str == "done" :
        break
    try:
        num_val = int(num_str)
    except:
        print("Invalid input")
        continue
    #print(num_val)
    if (largest is None):
        largest = num_val
    elif (num_val > largest):
        largest = num_val
    if (smallest is None):
        smallest = num_val
    elif (num_val < smallest):
        smallest = num_val


print("Maximum is", largest)
print("Minimum is", smallest)
