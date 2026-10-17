marks_levels = [25,40,55,65,78,85,95,97,34,12]
# Marks between 80 and 100 -> "Directly eligibe"
# Marks between 50 and 79 -> "needs training"
# Marks less that 50 -> "Not eligible"
# classify "invalid marks" (less that 0 and greater than 100)

for marks in marks_levels:
    if ((marks < 0) or (marks > 100)):
        print(f"{marks} -> invalid marks")
    elif ((marks >= 80) and (marks <=100)):
        print(f"{marks} -> Directly eligible")
    elif ((marks >= 50) and (marks <= 79)):
        print(f"{marks} -> needs training")
    else:
        print(f"{marks} -> Not eligible")
print("="*75)
courses = ["Core python", "SQL", "AI", "AIOps", "Adv Python", "Excel", "Python for DA"]
# return a list of courses that contains python or AI exactly in the above list
# python_or_ai_courses = [course for course in courses if "python" in course.lower() or "ai" in course.lower()]
python_or_ai_courses = []
for course in courses:
    if (("python" in course.lower()) or ("ai" in course.lower())):
        python_or_ai_courses.append(course)

print(f"Courses that contain `python` or `AI`: {python_or_ai_courses}")
print("="*75)
numbers = [12,15,22,30,45,60,75,82,90,100]
# write a program to create 3 categories of numbers based on the following conditions
# catogery_a : numbers divisible by 3 and 5
# catogery_b : numbers divisible by 2 and greater than 20
# catogery_c : all remaining numbers
# if a number is in catogery_a, it should not be in catogery_b or catogery_c

category_a = []
category_b = []
category_c = []
if len(numbers) > 0:
    for number in numbers:
        if ((number % 3 == 0) and (number % 5 == 0)):
            category_a.append(number)
        elif ((number % 2 == 0) and (number > 20)):
            category_b.append(number)
        else:
            category_c.append(number)

print(f"Category A (divisible by 3 and 5): {category_a}")
print(f"Category B (divisible by 2 and greater than 20): {category_b}")
print(f"Category C (all remaining numbers): {category_c}")
print("="*75)
# Python program that takes list of employees annual income and calculate the total income tax based on following slabes
# Upto 3 Lakhs -> tax rate is 0%
# from 3 Lakhs to 6 Lakhs -> tax rate is 5%
# from 6 Lakhs to 9 Lakhs -> tax rate is 10%
# from 9 Lakhs to 12 Lakhs -> tax rate is 15%
# above 12 Lakhs -> tax rate is 20%
# Output:
# income: 2500000, amount of tax deducted based on their income slab is 350000.0
# remaining amount after tax deduction is 2150000.0


incomes = [2500000, 1200000, 350000,7500000,16000000, 4500000, 3200000,1200000]
total_tax = 0

for income in incomes:
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = income * 0.05
    elif income <= 900000:
        tax = income * 0.10
    elif income <= 1200000:
        tax = income * 0.15
    else:
        tax = income * 0.20

    total_tax += tax
    remaining_amount = income - tax
    print(f"Income: {income}\n Amount of tax deducted based on their income slab is {tax}\n Remaining amount after tax deduction is {remaining_amount}")
    # print sum