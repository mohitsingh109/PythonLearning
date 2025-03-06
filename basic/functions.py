def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate
    return tax


print(calculate_tax(10000, 0.18))


def employee_details(name, department='Finance'):
    return f"{name} works in {department} department"


print(employee_details("Karan"))
print(employee_details("Mohit", "IT"))


def total(*amounts):
    return sum(amounts)


print(total(10, 20, 30, 40))

# Local & Global
company_name = "Company XYZ"  # Global


def department_info():
    company_name = "My Company"  # Local
    print(f"Company: {company_name}")


def department_info_global():
    global company_name
    print(f"Company: {company_name}")


department_info()
department_info_global()

