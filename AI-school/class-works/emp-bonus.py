employees = {"RAVI": 25000, "ANIL": 45000,"Vijay": 75000, "Vinay":55000}

# Give Annual Bonus to following employees based on their monthly salaries.

# salary below 30k -> 15%

# salary between 30k to 60k -> 10%

# Salary above 60k -> 5%

#output: name, salary, bonus,  total: salary
for k,v in employees.items():
    name = k
    salary = v
    if salary < 30000:
        bonus = salary * 0.15
    elif 30000 <= salary <= 60000:
        bonus = salary * 0.10
    else:
        bonus = salary * 0.05
    total_salary = salary + bonus
    print(f"Name: {name}\n Salary: {salary}\n Bonus: {bonus}\n Total Salary: {total_salary}")
    print(" -" * 20)

    