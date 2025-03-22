# For, while, Do while

# Print 1 to 5
for i in range(1, 6):
    print(i)
print("========")
students = ["Mohit", "Karan", "Aryan", 10]
for name in students:
    print(name, type(name))
print("========")
count = 5
while count > 0:
    print(count)
    count -= 1

print("========")
for num in range(1, 10):
    if num == 5:
        continue # skip
    print(num)

print("========")
for num in range(1, 10):
    if num == 5:
        break # stop
    print(num)
print("========")

for num in range(1, 10):
    if num == 5:
        continue # stop
    elif num == 8:
        break
    print(num)
print("========")