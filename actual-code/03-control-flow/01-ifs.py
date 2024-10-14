num1 = 14

if num1 > 11:
    print("Number is big!")
    print("Large numbers are cool.")
else:
    print("Small number")

if num1 % 2 == 0:
    print("This is an even number")

print("I'm doing more work down here")

if num1 > 0:
    if num1 % 2 == 0:
        print("This is an even positive number")
    else:
        print("This is an odd positive number")
else:
    if num1 % 2 == 0:
        print("Thsi is an even ngative number")
    else:
        print("This is an odd negative number.")

if num1 > 0 and num1 % 2 == 0:
    print("This is a postive even number.")

if num1 > 0 or num1 % 2 == 0:
    print("This is an even number or a positive number")

if not num1 > 0:
    print("This is a negative number.")

# Ternary

# test ? true_result : false_result

result = "positive number" if num1 > 0 else "negative number"

result = ""

if num1 > 0:
    result = "positive number"
else:
    result = "negative number"












