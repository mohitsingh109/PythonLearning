# List
employees = ["Mohit", "Aman", "Karan"]

print(employees[0])
print(employees[-1])
print(employees[-2])

employees.append("David")
print(employees)

employees.remove("Aman")
print(employees)

print(len(employees))

team_member = ["A", "B", "C", "D", "E"]
print(team_member[1:4])

# Tuples
status = ("RUN", "V1", "V2", "SCAN-AUDIT")
print(status[0])

company_info = [("TechCop", "Software", 5000), ("Tenable", "Cyber", 2500)]
print(company_info)

# Set (Unique value)
department = {"HR", "IT", "IT", "HR", "Finance"}
print(department)
department.add("ABC")
print(department)
department.remove("ABC")
print(department)

# Dict (K:Y)

employee_data = {
    "name": "John",
    "age": 30,
    "department": "IT"
}

print(employee_data)
print(employee_data.items())

for key, value in employee_data.items():
    print(f"key={key}, value={value}")