# Data type
num = 10
price = 99.99
name = "Mohit"
is_active = True

print(type(name))
print(type(price))
print(type(is_active))
print(type(num))


# Identation

def greet():
    print("I am working inside greet")

str_float = str(price)
print(str_float)
data = "67.89"
float_data = float(data)
print(float_data)


# input
# product_name = input("Enter the product name:")
# price = float(input("Enter the price"))
# print(f"The product {product_name} costs {price}")

a = 10
b = 3

print(a / b)
print(a // b)
print(a ** b)

# > , <=, !=, <> (Not equal to)

# Logical operator
# and (&&), or (||) not(!)

age = 10
salary = 50000
print(age > 5 and salary > 500)
print(age > 50 or salary > 600)
print(not age > 70)

# Assignment operator
# ++, --
x = 10
x += 1

# Short Circuit evaluation
print(age > 50 and salary > 500)

# Operator Precedence
"""
()
*, /,
+, -
>=
"""
result = (5 + 2) * 3
print(result)

