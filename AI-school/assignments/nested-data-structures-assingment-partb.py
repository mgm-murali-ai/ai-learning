print("*" * 72)
print("*" * 15 + " PART B: NETED DATA STRUCTURES ASSIGNMENT " + "*" * 15)
print("*" * 72)
print(" ")
print("*" * 10 + "Question-11. E-commerce cart billing " + "*" * 10)
question_11 = """
Question-11. E-commerce cart billing
Structure: List of dictionaries with a price/quantity tupleQ
Starter data
cart = [{"product":"Laptop","category":"Electronics","details":(55000,1)}, {"product":"Mouse","category":"Accessories","details":(800,2)}, {"product":"Keyboard","category":"Accessories","details":(2500,1)}, {"product":"Monitor","category":"Electronics","details":(12000,1)}]
Task: Print each product and line amount; apply 10% discount for Electronics, 5% for Accessories, otherwise zero; calculate total payable; build a list of products whose original line amount exceeds ₹10,000.
"""
print(question_11)
cart = [
    {"product": "Laptop", "category": "Electronics", "details": (55000, 1)},
    {"product": "Mouse", "category": "Accessories", "details": (800, 2)},
    {"product": "Keyboard", "category": "Accessories", "details": (2500, 1)},
    {"product": "Monitor", "category": "Electronics", "details": (12000, 1)},
]
exceeded_products = []
exceeded_products_after_discount = []
for item in cart:
    product = item["product"]
    category = item["category"]
    product_details = item["details"]
    product_price = product_details[0]
    product_quantity = product_details[1]
    line_amount = product_price * product_quantity
    if category == "Electronics":
        discount = 0.10 * line_amount
        total_amount_after_discount = line_amount - discount
    elif category == "Accessories":
        discount = 0.05 * line_amount
        total_amount_after_discount = line_amount - discount
    else:
        discount = 0
        total_amount_after_discount = line_amount - discount
    discounted_amount = line_amount - discount
    print(
        f"Product: {product}\n Category: {category}\n Line Amount(Before Discount): ₹{line_amount}\n Discounted Amount: ₹{discounted_amount}\n Total Amount After Discount: ₹{total_amount_after_discount}"
    )
    print(" -" * 20)
    if line_amount > 10000:
        exceeded_products.append(product)
    if total_amount_after_discount > 10000:
        exceeded_products_after_discount.append(product)
print(f"Products with line amount exceeding ₹10,000: {exceeded_products}")
print(
    f"Products with discounted amount exceeding ₹10,000: {exceeded_products_after_discount}"
)
print("=" * 60)
print("*" * 10 + "Question-12. Office device assignment " + "*" * 10)
question_12 = """
Question-12. Office device assignment
Structure: Dictionary of dictionaries with tuple
Starter data
{"EMP1":{"name":"Ravi","device":("Laptop","Assigned")},"EMP2":{"name":"Anu","device":("Monitor","Pending")},"EMP3":{"name":"Sai","device":("Keyboard","Assigned")}}
Task: Create a dictionary mapping employee IDs to Ready when device status is Assigned, otherwise Awaiting Device.
"""
print(question_12)
employee_data = {
    "EMP1": {"name": "Ravi", "device": ("Laptop", "Assigned")},
    "EMP2": {"name": "Anu", "device": ("Monitor", "Pending")},
    "EMP3": {"name": "Sai", "device": ("Keyboard", "Assigned")},
}
for emp_id, emp_info in employee_data.items():
    device_status = emp_info["device"][1]
    if device_status == "Assigned":
        emp_id = emp_id
        emp_name = emp_info["name"]
        emp_device = emp_info["device"][0]
        employee_data[emp_id]["status"] = "Ready"
        print(
            f"Employee ID: {emp_id}\n Employee Name: {emp_name}\n Device: {emp_device}\n Device Status: {device_status}\n Status: Ready"
        )
        print(" -" * 20)
    else:
        employee_data[emp_id]["status"] = "Awaiting Device"
        print(
            f"Employee ID: {emp_id}\n Employee Name: {emp_name}\n Device: {emp_device}\n Device Status: {device_status}\n Status: Awaiting Device"
        )
        print(" -" * 20)
print("=" * 60)
print("*" * 10 + "Question-13. Grocery basket discount " + "*" * 10)
question_13 = """
Question-13. Grocery basket discount
Structure: List of dictionaries with tuple
Starter data
[{"name":"Rice","purchase":(1200,2)},{"name":"Oil","purchase":(650,1)},{"name":"Sugar","purchase":(80,3)}]
Task: Tuple is (unit price, quantity). Apply 8% discount to line totals >=2000, 3% for totals >=500, otherwise 0%. Create dictionary mapping item name to discounted line total.
"""
print(question_13)
grocery_basket = [
    {"name": "Rice", "purchase": (1200, 2)},
    {"name": "Oil", "purchase": (650, 1)},
    {"name": "Sugar", "purchase": (80, 3)},
]
discounted_totals = {}

for item in grocery_basket:
    purchase_details = item["purchase"]
    unit_price = purchase_details[0]
    unit_quantity = purchase_details[1]
    line_total = unit_price * unit_quantity

    if line_total >= 2000:
        grocery_name = item["name"]
        discounted_amount = line_total * 0.08
        discounted_total = line_total - discounted_amount
        # print(f"Grocery Item: {grocery_name}\n Original Line Total: ₹{line_total}\n Discounted Amount: ₹{discounted_amount}\n Discounted Line Total: ₹{discounted_total}")
        # print(" -" * 20)
    elif line_total >= 500:
        grocery_name = item["name"]
        discounted_amount = line_total * 0.03
        discounted_total = line_total - discounted_amount
        # print(f"Grocery Item: {grocery_name}\n Original Line Total: ₹{line_total}\n Discounted Amount: ₹{discounted_amount}\n Discounted Line Total: ₹{discounted_total}")
        # print(" -" * 20)
    else:
        grocery_name = item["name"]
        discounted_amount = 0
        discounted_total = line_total - discounted_amount
        # print(f"Grocery Item: {grocery_name}\n Original Line Total: ₹{line_total}\n Discounted Amount: ₹{discounted_amount}\n Discounted Line Total: ₹{discounted_total}")
        # print(" -" * 20)

    print(
        f"Grocery Item: {grocery_name}\n Original Line Total: ₹{line_total}\n Discounted Amount: ₹{discounted_amount}\n Discounted Line Total: ₹{discounted_total}"
    )
    print(" -" * 20)
    discounted_totals[item["name"]] = discounted_total

# print(" "+"-" * 10 + "  Discounted Line Totals: " + "-" * 10)
# for item_name, total in discounted_totals.items():
#     print(f"Grocery Item: {item_name}\n Discounted Line Total: ₹{total}")
print("=" * 60)

question_14 = """
Question-14. Bank account balance alerts
Structure: Dictionary of dictionaries
Starter data
{"A101":{"holder":"Ravi","balance":2500,"type":"Savings"},"A102":{"holder":"Anu","balance":55000,"type":"Current"},"A103":{"holder":"Sai","balance":900,"type":"Savings"}}
Task: Create account-ID-to-alert dictionary: Critical if balance <1000, Low Balance if balance <5000 and type is Savings, otherwise Healthy.
"""
print("*" * 10 + " Question-14: Bank Account Balance Alerts " + "*" * 10)
print(question_14)
bank_accounts = {
    "A101": {"holder": "Ravi", "balance": 2500, "type": "Savings"},
    "A102": {"holder": "Anu", "balance": 55000, "type": "Current"},
    "A103": {"holder": "Sai", "balance": 900, "type": "Savings"},
}
# account_alerts = {}

for account_id, details in bank_accounts.items():
    account_id = account_id.strip()
    account_holder = details["holder"]
    balance = details["balance"]
    account_type = details["type"]

    if balance < 1000:
        alert = "Critical"
    elif balance < 5000 and account_type == "Savings":
        alert = "Low Balance"
    else:
        alert = "Healthy"

    print(
        f"Account ID: {account_id}\n Account Holder: {account_holder}\n Account Type: {account_type}\n Balance: ₹{balance}\n Alert: {alert}"
    )
    print(" -" * 20)
    # account_alerts[account_id] = alert

# print("Account Alerts:")
# for account_id, alert in account_alerts.items():
#     print(f"Account ID: {account_id}\n Alert: {alert}")
print("=" * 60)
question_15 = """
15. Exam subject performance
Structure: Dictionary of student dictionaries with marks tuple
Starter data
{"Rahul":{"marks":(80,75,90),"stream":"AI"},"Anu":{"marks":(50,55,60),"stream":"Data"},"Kiran":{"marks":(30,45,40),"stream":"AI"}}
Task: Compute average from tuple; build dictionary with Excellent if >=80, Pass if >=40, otherwise Review.
"""
print("*" * 10 + " Question-15: Exam Subject Performance " + "*" * 10)
print(question_15)
exam_performance = {
    "Rahul": {"marks": (80, 75, 90), "stream": "AI"},
    "Anu": {"marks": (50, 55, 60), "stream": "Data"},
    "Kiran": {"marks": (30, 45, 40), "stream": "AI"},
}
# performance_alerts = {}

for student, details in exam_performance.items():
    student = student.strip()
    marks = details["marks"]
    stream = details["stream"]
    average = sum(marks) / len(marks)

    if average >= 80:
        alert = "Excellent"
    elif average >= 40:
        alert = "Pass"
    else:
        alert = "Review"

    print(f"Student: {student}\n Stream: {stream}\n Marks: {marks}\n Average: {average:.2f}\n Alert: {alert}")
    print(" -" * 20)
    # performance_alerts[student] = alert

print("=" * 60)
question_16 = """
Question-16. Courier shipment tracking
Structure: List of dictionaries with status tuple
Starter data
[{"id":"S101","route":("Hyderabad","Vijayawada"),"days":1},{"id":"S102","route":("Delhi","Hyderabad"),"days":5},{"id":"S103","route":("Chennai","Bengaluru"),"days":3}]
Task: Create shipment-ID-to-status dictionary: On Time if days <=2; Delayed if days 3–4; Escalate otherwise. Print origin and destination.
"""
print("*" * 10 + " Question-16: Courier Shipment Tracking " + "*" * 10)
print(question_16)
print("*" * 60)
shipments = [
    {"id": "S101", "route": ("Hyderabad", "Vijayawada"), "days": 1},
    {"id": "S102", "route": ("Delhi", "Hyderabad"), "days": 5},
    {"id": "S103", "route": ("Chennai", "Bengaluru"), "days": 3},
]

for shipment in shipments:
    shipment_id = shipment["id"].strip()
    shipment_route = shipment["route"]
    shipment_origin = shipment_route[0]
    shipment_destination = shipment_route[1]
    shipment_days = shipment["days"]

    if shipment_days <= 2:
        status = "On Time"
    elif 3 <= shipment_days <= 4:
        status = "Delayed"
    else:
        status = "Escalate"

    print(f"Shipment ID: {shipment_id}\n Origin: {shipment_origin}\n Destination: {shipment_destination}\n Days: {shipment_days}\n Status: {status}")
    print(" -" * 20)
print("=" * 60)
question_17 = """
Question-17. IT helpdesk triage
Structure: Dictionary of ticket dictionaries
Starter data
{"T1":{"hours":8,"tags":{"production","urgent"}},"T2":{"hours":2,"tags":{"password"}},"T3":{"hours":5,"tags":{"network"}}}
Task: Create ticket-ID-to-priority dictionary: Critical if hours >=6 or urgent tag exists; Medium if hours >=3; Low otherwise.
"""
print("*" * 10 + " Question-17: IT Helpdesk Triage " + "*" * 10)
print(question_17)
print("-*" * 60)
tickets = {
    "T1": {"hours": 8, "tags": {"production", "urgent"}},
    "T2": {"hours": 2, "tags": {"password"}},
    "T3": {"hours": 5, "tags": {"network"}},
}

for ticket_id, details in tickets.items():
    ticket_id = ticket_id.strip()
    hours = details["hours"]
    tags = details["tags"]

    if hours >= 6 or "urgent" in tags:
        priority = "Critical"
    elif hours >= 3:
        priority = "Medium"
    else:
        priority = "Low"

    print(f"Ticket ID: {ticket_id}\n Hours: {hours}\n Tags: {tags}\n Priority: {priority}")
    print(" -" * 20)
print("=" * 60)
question_18 = """
Question-18. Gym membership renewal
Structure: List of dictionaries with tuple
Starter data
[{"name":"Anu","membership":("Gold",2)},{"name":"Ravi","membership":("Basic",0)},{"name":"Meena","membership":("Gold",10)}]
Task: Tuple contains (plan, days remaining). Create name-to-reminder dictionary: Expired if days <=0; Renew Soon if days <=3 or plan is Basic and days <=7; otherwise Active.
"""
print("*" * 10 + " Question-18: Gym Membership Renewal " + "*" * 10)
print(question_18)
print("-*" * 60)
memberships = [
    {"name": "Anu", "membership": ("Gold", 2)},
    {"name": "Ravi", "membership": ("Basic", 0)},
    {"name": "Meena", "membership": ("Gold", 10)},
]

for member in memberships:
    name = member["name"].strip()
    membership_details = member["membership"]
    membership_plan = membership_details[0]
    days_remaining = membership_details[1]

    if (days_remaining <= 0):
        reminder = "Expired"
    elif (days_remaining <= 3 or (membership_plan == "Basic" and days_remaining <= 7)):
        reminder = "Renew Soon"
    else:
        reminder = "Active"

    print(f"Name: {name}\n Plan: {membership_plan}\n Days Remaining: {days_remaining}\n Reminder: {reminder}")
    print(" -" * 20)
print("=" * 60)
question_19 = """
Question-19. Employee payroll and performance
Structure: Dictionary of employee dictionaries containing tuples and lists
Starter data
employees = {"EMP101":{"name":"Ravi","salary":50000,"ratings":(4,5,4),"projects":["Chatbot","RAG"]}, "EMP102":{"name":"Anu","salary":65000,"ratings":(3,3,4),"projects":["API","Automation","AI Agent"]}, "EMP103":{"name":"Kiran","salary":40000,"ratings":(2,3,2),"projects":["Dashboard"]}}
Task: For each employee, calculate average rating and project count; apply 20% increment if average >=4 and projects >=2; otherwise 10% if average >=3 or projects >=3; otherwise 0%; create a dictionary mapping employee name to updated salary.
"""
print("*" * 10 + " Question-19: Employee Payroll and Performance " + "*" * 10)
print(question_19)
print("-*" * 60)
employees = {
    "EMP101": {"name": "Ravi", "salary": 50000, "ratings": (4, 5, 4), "projects": ["Chatbot", "RAG"]},
    "EMP102": {"name": "Anu", "salary": 65000, "ratings": (3, 3, 4), "projects": ["API", "Automation", "AI Agent"]},
    "EMP103": {"name": "Kiran", "salary": 40000, "ratings": (2, 3, 2), "projects": ["Dashboard"]},
}

updated_salaries = {}

for emp_id, details in employees.items():
    name = details["name"].strip()
    salary = details["salary"]
    ratings = details["ratings"]
    projects = details["projects"]

    avg_rating = sum(ratings) / len(ratings)
    project_count = len(projects)

    if avg_rating >= 4 and project_count >= 2:
        increment = 0.2
    elif avg_rating >= 3 or project_count >= 3:
        increment = 0.1
    else:
        increment = 0.0

    updated_salary = salary * (1 + increment)
    updated_salaries[name] = updated_salary

    print(f"Name: {name}\n Average Rating: {avg_rating:.2f}\n Project Count: {project_count}\n Updated Salary: {updated_salary}")
    print(" -" * 20)
print("=" * 60)
question_20 = """
Question- 20. Patient review queue (simulation)
Structure: List of dictionaries with vitals tuple and symptoms set
Starter data
patients = [{"id":"P101","name":"Ramesh","age":65,"vitals":(145,95),"symptoms":{"fever","cough"}}, {"id":"P102","name":"Anu","age":28,"vitals":(118,78),"symptoms":{"headache"}}, {"id":"P103","name":"Kiran","age":45,"vitals":(135,88),"symptoms":{"fever","fatigue"}}]
Task: Treat vitals as (systolic, diastolic). Print Priority Review if systolic >=140 or diastolic >=90; Routine Review if systolic >=130 or age >=60; otherwise Standard. Build a list of Priority Review patient IDs. Fictional training logic, not medical advice.
"""
print("*" * 10 + " Question-20: Patient Review Queue (Simulation)" + "*" * 10)
print(question_20)
print("-*" * 60)
patients = [
    {"id": "P101", "name": "Ramesh", "age": 65, "vitals": (145, 95), "symptoms": {"fever", "cough"}},
    {"id": "P102", "name": "Anu", "age": 28, "vitals": (118, 78), "symptoms": {"headache"}},
    {"id": "P103", "name": "Kiran", "age": 45, "vitals": (135, 88), "symptoms": {"fever", "fatigue"}},
]

priority_review_ids = []

for patient in patients:
    systolic, diastolic = patient["vitals"]
    age = patient["age"]
    review_type = "Standard"

    if systolic >= 140 or diastolic >= 90:
        review_type = "Priority Review"
        priority_review_ids.append(patient["id"])
    elif systolic >= 130 or age >= 60:
        review_type = "Routine Review"

    print(f"ID: {patient['id']}\n Name: {patient['name']}\n Age: {age}\n Review Type: {review_type}")
    print(" -" * 20)

print(f"Priority Review Patient IDs: {priority_review_ids}")
print("=" * 60)
