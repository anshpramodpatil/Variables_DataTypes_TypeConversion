# TASK 2: Variables, Data Types & Type Conversion

# Declaring variables of different types: int, float, string, boolean.
age = 20
weight = 5.10
name = "Ansh Pramod Patil"
is_student = True;

print("Age:",age)
print("Weight:",weight, "kg")
print("Name:",name)
print("Is Student:",is_student)

print("\n")

# Printing the type of each variable using type().
print("Type of age:", type(age))
print("Type of weight:", type(weight))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))
print("\n")

# Performing arithmetic operations using numeric variables
num1 = 4
num2 = 5

total = num1 + num2
product = num1 * num2

print("Arithmatic equations")
print("1st Number: ",num1)
print("2nd Number: ",num2)
print("Sum of both values:", total)
print("Product of both values:", product)
print("\n")

# Converting string input to integer and float using type casting & using try-except block to handle invalid input
try:
    ageInput = input("Enter the age:")
    weightInput = input("Enter the weight:")

    age_Int = int(ageInput)
    weight_Float = float(weightInput)

    print("Age:", age_Int, "& Type:", type(age_Int))
    print("Weight: ", weight_Float, "kg & Type:", type(weight_Float))

except ValueError:
    print("Please enter the numeric values only..")

print("\n")

# Concatenating strings and numbers properly
result = name + " is " + str(age) + " years old"
print(result)
print("\n")

# Demonstrating dynamic typing by reassigning variable values
value = 10
print("Value: ",value, "& Type: ",type(value))

value = 10.5
print("Value: ",value, "& Type: ", type(value))

value = "Ansh"
print("Value: ",value, "& Type: ", type(value))

value = True
print("Value: ",value, "& Type: ", type(value))
print("\n")