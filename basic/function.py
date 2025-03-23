
# Function with no args
def print_name():
    print("Hi..")

print_name()

# Function with one args
def print_name(name):
    print(f"Hi.. {name}")

print_name("Mohit")

# Function with more then one args (default values)
def employee_details(name, department='Finance'):
    print(f"Name: {name}, Department: {department}")

employee_details("Mohit", "IT")
employee_details("Aryan")

# How to return value from function
def calculate_score(eng, math, science):
    total = eng + math + science
    return total

total_score = calculate_score(90, 70, 88)
print(f"Total score: {total_score}")


# Global v