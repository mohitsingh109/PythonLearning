# if elif else

temperature = 30

if temperature > 35:
    print("It's to hot! Stay inside")
elif 25 <= temperature <= 35:
    print("This weather is nice")
else:
    print("It's bit cold wear a jacket")

# for, while loop

fruits = ["apple", "orange", "cherry"]

for fruit in fruits:
    print(fruit)

for retry in range(1, 6):  # loop from 1 to 5
    print(retry)

count = 5
while count > 0:
    print(f"Count = {count}")
    count -= 1

for num in range(1, 10):  # loop from 1 to 5
    if num == 5:
        break
    print(num)

for num in range(1, 10):
    if num == 5:
        continue
    print(num)
