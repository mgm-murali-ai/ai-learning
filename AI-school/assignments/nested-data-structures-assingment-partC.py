print("-" * 73)
print("*" * 15 + " PART C: NESTED DATA STRUCTURES ASSIGNMENT " + "*" * 15)
print("-" * 73)
print(" ")

question_21 = """
Question-21. Insurance premium estimate (fictional)
Structure: Dictionary with age and coverage tuple
Starter data
{"C101":{"age":25,"coverage":(500000,1)},"C102":{"age":45,"coverage":(1000000,2)},"C103":{"age":62,"coverage":(500000,1)}}
Task: Tuple is (coverage_amount, members). Calculate fictional premium = coverage_amount * rate * members, using 1% if age <35, 2% if age <=55, otherwise 3%. Build customer-ID-to-premium dictionary.
"""
print("*" * 10 + " Question-21: Insurance Premium Estimate (Fictional) " + "*" * 10)
print(question_21)
print("-*" * 60)
insurance_data = {
    "C101": {"age": 25, "coverage": (500000, 1)},
    "C102": {"age": 45, "coverage": (1000000, 2)},
    "C103": {"age": 62, "coverage": (500000, 1)},
}

premiums = {}

for cust_id, details in insurance_data.items():
    age = details["age"]
    insurance_coverage = details["coverage"]
    insurance_coverage_amount = insurance_coverage[0]
    insurance_coverage_members = insurance_coverage[1]

    if age < 35:
        rate = 0.01
    elif age <= 55:
        rate = 0.02
    else:
        rate = 0.03

    premium = insurance_coverage_amount * rate * insurance_coverage_members
    premiums[cust_id] = premium

    print(f"Customer ID: {cust_id}\n Age: {age}\n Coverage Amount: {insurance_coverage_amount}\n Members: {insurance_coverage_members}\n Premium: {premium}")
    print(" -" * 20)

print(f"Customer ID to Premium Mapping: {premiums}")
print("=" * 60)
question_22 = """
Question-22. Event registration validation
Structure: Dictionary of dictionaries with sets
Starter data
{"R1":{"name":"Anu","passes":{"Workshop","Hackathon"},"paid":1500},"R2":{"name":"Ravi","passes":{"Workshop"},"paid":500},"R3":{"name":"Sai","passes":{"Hackathon"},"paid":0}}
Task: Build registration-ID-to-status dictionary: Complete if paid >=1000 and Hackathon pass exists; Workshop Only if paid >=500 and Workshop pass exists; otherwise Pending.
"""
print("*" * 10 + " Question-22: Event Registration Validation " + "*" * 10)
print(question_22)
print("-*" * 60)
registration_data = {
    "R1": {"name": "Anu", "passes": {"Workshop", "Hackathon"}, "paid": 1500},
    "R2": {"name": "Ravi", "passes": {"Workshop"}, "paid": 500},
    "R3": {"name": "Sai", "passes": {"Hackathon"}, "paid": 0},
}

status = {}

for reg_id, details in registration_data.items():
    paid = details["paid"]
    passes = details["passes"]

    if paid >= 1000 and "Hackathon" in passes:
        reg_status = "Complete"
    elif paid >= 500 and "Workshop" in passes:
        reg_status = "Workshop Only"
    else:
        reg_status = "Pending"

    status[reg_id] = reg_status

    print(f"Registration ID: {reg_id}\n Name: {details['name']}\n Passes: {passes}\n Paid: {paid}\n Status: {reg_status}")
    print(" -" * 20)

print(f"Registration ID to Status Mapping: {status}")
print("=" * 60)
question_23 = """
Question- 23. Hotel room housekeeping
Structure: List of dictionaries with tuple and set
Starter data
[{"room":"101","state":("Vacant",2),"issues":{"towels"}},{"room":"102","state":("Occupied",0),"issues":set()},{"room":"103","state":("Vacant",0),"issues":set()}]
Task: Tuple means (occupancy, hours_since_clean). Create room-to-action dictionary: Clean Now if vacant and hours >=2 or issues set is nonempty; Ready if vacant and no issues; otherwise Occupied.
"""
print("*" * 10 + " Question-23: Hotel Room Housekeeping " + "*" * 10)
print(question_23)
print("-*" * 60)
room_data = [
    {"room": "101", "state": ("Vacant", 2), "issues": {"towels"}},
    {"room": "102", "state": ("Occupied", 0), "issues": set()},
    {"room": "103", "state": ("Vacant", 0), "issues": set()},
]

room_action = {}

for room in room_data:
    room_number = room["room"]
    room_state = room["state"]
    room_issues = room["issues"]
    room_ocupancy = room_state[0]
    hours_since_clean = room_state[1]

    if (room_ocupancy == "Vacant" and (hours_since_clean >= 2 or room_issues)):
        action = "Clean Now"
    elif (room_ocupancy == "Vacant" and not room_issues):
        action = "Ready"
    else:
        action = "Occupied"

    room_action[room_number] = action

    print(f"Room: {room_number}\n State: {room['state']}\n Issues: {room_issues}\n Action: {action}")
    print(" -" * 20)

print(f"Room to Action Mapping: {room_action}")
print("=" * 60)
question_24 = """
Question- 24. Retail return eligibility
Structure: Dictionary of order dictionaries
Starter data
{"O1":{"product":"Shoes","days":5,"tags":{"unused"}},"O2":{"product":"Headphones","days":18,"tags":{"opened"}},"O3":{"product":"Bag","days":9,"tags":{"unused"}}}
Task: Create order-ID-to-decision dictionary: Eligible if days <=10 and unused tag exists; Review if days <=15 or opened tag exists; otherwise Rejected. Fictional store policy.
"""
print("*" * 10 + " Question-24: Retail Return Eligibility " + "*" * 10)
print(question_24)
print("-*" * 60)
order_data = {
    "O1": {"product": "Shoes", "days": 5, "tags": {"unused"}},
    "O2": {"product": "Headphones", "days": 18, "tags": {"opened"}},
    "O3": {"product": "Bag", "days": 9, "tags": {"unused"}},
}

decision = {}

for order_id, details in order_data.items():
    days = details["days"]
    tags = details["tags"]

    if days <= 10 and "unused" in tags:
        order_decision = "Eligible"
    elif days <= 15 or "opened" in tags:
        order_decision = "Review"
    else:
        order_decision = "Rejected"

    decision[order_id] = order_decision

    print(f"Order ID: {order_id}\n Product: {details['product']}\n Days: {days}\n Tags: {tags}\n Decision: {order_decision}")
    print(" -" * 20)

print(f"Order ID to Decision Mapping: {decision}")
print("=" * 60)
question_25 = """ 
Question- 25. Campus placement shortlist (simulation)
Structure: Dictionary of student dictionaries with tuple and set
Starter data
{"S1":{"name":"Asha","scores":(88,92),"skills":{"Python","SQL","GenAI"}},"S2":{"name":"Ravi","scores":(70,74),"skills":{"Python"}},"S3":{"name":"Meena","scores":(90,85),"skills":{"Python","RAG"}}}
Task: Calculate average scores; build student-ID-to-status dictionary: Shortlist if average >=85 and Python is in skills and (GenAI or RAG is in skills); Train More if average >=70; otherwise Foundation. Fictional screening rule.
"""
print("*" * 10 + " Question-25: Campus Placement Shortlist " + "*" * 10)
print(question_25)
print("-*" * 60)
student_data = {
    "S1": {"name": "Asha", "scores": (88, 92), "skills": {"Python", "SQL", "GenAI"}},
    "S2": {"name": "Ravi", "scores": (70, 74), "skills": {"Python"}},
    "S3": {"name": "Meena", "scores": (90, 85), "skills": {"Python", "RAG"}},
}

status = {}

for student_id, details in student_data.items():
    scores = details["scores"]
    skills = details["skills"]
    average_score = sum(scores) / len(scores)

    if average_score >= 85 and "Python" in skills and ("GenAI" in skills or "RAG" in skills):
        student_status = "Shortlist"
    elif average_score >= 70:
        student_status = "Train More"
    else:
        student_status = "Foundation"

    status[student_id] = student_status

    print(f"Student ID: {student_id}\n Name: {details['name']}\n Scores: {scores}\n Skills: {skills}\n Average: {average_score}\n Status: {student_status}")
    print(" -" * 20)

print(f"Student ID to Status Mapping: {status}")
print("=" * 60)
question_26 = """ 
Question- 26. Subscription renewal billing
Structure: Dictionary of customer dictionaries with tuple
Starter data
{"C1":{"plan":("Pro",999),"days_left":2},"C2":{"plan":("Basic",299),"days_left":12},"C3":{"plan":("Pro",999),"days_left":0}}
Task: Build customer-ID-to-result dictionary: Expired if days_left <=0; Renew Soon if days_left <=3; Active otherwise. Print monthly price from tuple.
"""
print("*" * 10 + " Question-26: Subscription Renewal Billing " + "*" * 10)
print(question_26)
print("-*" * 60)
customer_data = {
    "C1": {"plan": ("Pro", 999), "days_left": 2},
    "C2": {"plan": ("Basic", 299), "days_left": 12},
    "C3": {"plan": ("Pro", 999), "days_left": 0},
}
customer_status = {}
for customer_id, details in customer_data.items():
    cust_id = customer_id
    cust_plan = details["plan"]
    cust_days_left = details["days_left"]
    plan_price = details["plan"][1]

    if cust_days_left <= 0:
        cust_status = "Expired"
    elif cust_days_left <= 3:
        cust_status = "Renew Soon"
    else:
        cust_status = "Active"

    customer_status[customer_id] = cust_status

    print(f"Customer ID: {customer_id}\n Plan: {cust_plan}\n Price: {plan_price}\n Days Left: {cust_days_left}\n Status: {cust_status}")
    print(" -" * 20)

print(f"Customer ID to Status Mapping: {customer_status}")
print("=" * 60)
question_27 = """ 
Question- 27. AI project portfolio review
Structure: Dictionary of student dictionaries containing lists and sets
Starter data
{"ST1":{"name":"Anu","projects":["RAG Bot","Agent"],"skills":{"Python","GenAI"}},"ST2":{"name":"Ravi","projects":["Calculator"],"skills":{"Python"}},"ST3":{"name":"Meena","projects":["Chatbot","Resume Analyzer","RAG"],"skills":{"Python","SQL","RAG"}}}
Task: Build student-ID-to-review dictionary: Strong Portfolio if projects >=2 and (GenAI or RAG in skills); Growing Portfolio if projects >=2 or Python in skills; otherwise Start Building. Also collect strong-portfolio names in a list.
"""
print("*" * 10 + " Question-27: AI Project Portfolio Review " + "*" * 10)
print(question_27)
print("-*" * 60)

student_data = {
    "ST1": {"name": "Anu", "projects": ["RAG Bot", "Agent"], "skills": {"Python", "GenAI"}},
    "ST2": {"name": "Ravi", "projects": ["Calculator"], "skills": {"Python"}},
    "ST3": {"name": "Meena", "projects": ["Chatbot", "Resume Analyzer", "RAG"], "skills": {"Python", "SQL", "RAG"}},
}
student_review = {}
strong_portfolio_names = []
for student_id, details in student_data.items():
    name = details["name"]
    projects = details["projects"]
    skills = details["skills"]

    if (len(projects) >= 2 and ("GenAI" in skills or "RAG" in skills)):
        review = "Strong Portfolio"
        strong_portfolio_names.append(name)
    elif len(projects) >= 2 or "Python" in skills:
        review = "Growing Portfolio"
    else:
        review = "Start Building"

    student_review[student_id] = review

    print(f"Student ID: {student_id}\n Name: {name}\n Projects: {projects}\n Skills: {skills}\n Review: {review}")
    print(" -" * 20)

print(f"Student ID to Review Mapping: {student_review}")
print(f"Strong Portfolio Names: {strong_portfolio_names}")
print("=" * 60)
question_28 = """ 
Question- 28. AI School student learning analytics
Structure: Dictionary of student dictionaries combining all five structures
Starter data
students = {"ST101":{"name":"Rahul","course":"Launchpad","marks":[85,90,88],"projects":("Chatbot","Resume Analyzer"),"skills":{"Python","SQL","GenAI"},"fees_paid":22000}, "ST102":{"name":"Anu","course":"Accelerator","marks":[92,95,90],"projects":("RAG","AI Agent","Automation"),"skills":{"Python","GenAI","LangGraph"},"fees_paid":20000}, "ST103":{"name":"Kiran","course":"Launchpad","marks":[55,65,60],"projects":("Calculator",),"skills":{"Python","SQL"},"fees_paid":11000}, "ST104":{"name":"Priya","course":"Accelerator","marks":[78,82,80],"projects":("Chatbot","RAG"),"skills":{"Python","GenAI"},"fees_paid":10000}}
Task: Calculate average marks and project count; determine course fee (Launchpad ₹22,000; Accelerator ₹20,000); classify Placement Ready if average >=85 and projects >=2 and fee fully paid; On Track if average >=70 or projects >=2; otherwise Needs Improvement. Create student-ID-to-status dictionary and a list of Placement Ready names. Labels are for practice only.
"""
print("*" * 10 + " Question-28: AI School student learning analytics " + "*" * 10)
print(question_28)
print("-*" * 60)
student_data = {
    "ST101": {"name": "Rahul", "course": "Launchpad", "marks": [85, 90, 88], "projects": ("Chatbot", "Resume Analyzer"), "skills": {"Python", "SQL", "GenAI"}, "fees_paid": 22000},
    "ST102": {"name": "Anu", "course": "Accelerator", "marks": [92, 95, 90], "projects": ("RAG", "AI Agent", "Automation"), "skills": {"Python", "GenAI", "LangGraph"}, "fees_paid": 20000},
    "ST103": {"name": "Kiran", "course": "Launchpad", "marks": [55, 65, 60], "projects": ("Calculator",), "skills": {"Python", "SQL"}, "fees_paid": 11000},
    "ST104": {"name": "Priya", "course": "Accelerator", "marks": [78, 82, 80], "projects": ("Chatbot", "RAG"), "skills": {"Python", "GenAI"}, "fees_paid": 10000}
}
student_status = {}
placement_ready_names = []
for student_id, details in student_data.items():
    name = details["name"]
    course = details["course"]
    marks = details["marks"]
    projects = details["projects"]
    fees_paid = details["fees_paid"]

    avg_marks = sum(marks) / len(marks)
    project_count = len(projects)
    course_fee = 22000 if course == "Launchpad" else 20000

    if avg_marks >= 85 and project_count >= 2 and fees_paid >= course_fee:
        status = "Placement Ready"
        placement_ready_names.append(name)
    elif avg_marks >= 70 or project_count >= 2:
        status = "On Track"
    else:
        status = "Needs Improvement"

    student_status[student_id] = status
    print(f"Student ID {student_id}\n student name: {name}\n course: {course}\n average marks: {avg_marks}\n project count: {project_count}\n fees paid: {fees_paid}\n Status {status}")
    print(" -" * 20)
print(f"Student ID to Status Mapping: {student_status}")
print(f"Placement Ready Names: {placement_ready_names}")
print("=" * 60)

question_29 = """
Question- 29. Cafeteria meal token checker
Structure: Dictionary with nested tuples and sets
Starter data
{"T1":{"meal":("Lunch",120),"extras":{"Juice"}},"T2":{"meal":("Breakfast",70),"extras":set()},"T3":{"meal":("Dinner",160),"extras":{"Dessert"}}}
Task: Create token-to-total dictionary. Add ₹30 if Juice is in extras, otherwise add ₹40 if Dessert is in extras, otherwise add zero. Use one loop.
"""
print("*" * 10 + " Question-29: Cafeteria meal token checker " + "*" * 10)
print(question_29)
print("-*" * 60)

cafeteria_data = {
    "T1": {"meal": ("Lunch", 120), "extras": {"Juice"}},
    "T2": {"meal": ("Breakfast", 70), "extras": set()},
    "T3": {"meal": ("Dinner", 160), "extras": {"Dessert"}}
}

token_to_total = {}
for token, details in cafeteria_data.items():
    cafeteria_counter_no = token
    meal_price = details["meal"][1]
    extras = details["extras"]
    extra_charge = 0
    if "Juice" in extras:
        extra_charge = 30
    elif "Dessert" in extras:
        extra_charge = 40
    total = meal_price + extra_charge
    token_to_total[token] = total
    print(f"Cafeteria Counter No: {cafeteria_counter_no}\n Meal Price: {meal_price}\n Extras: {extras}\n Extra Charge: {extra_charge}\n Total: {total}")
    print(" -" * 20)

print(f"Token to Total Mapping: {token_to_total}")
print("=" * 60)
question_30 = """
Question- 30. Online course completion certificates
Structure: List of dictionaries containing lists and tuples
Starter data
[{"name":"Anu","progress":(92,3),"modules":["Python","SQL"]},{"name":"Ravi","progress":(68,1),"modules":["Python"]},{"name":"Meena","progress":(100,4),"modules":["Python","SQL","AI"]}]
Task: Tuple is (completion_percent, projects). Create name-to-status dictionary: Certificate Ready if completion >=90 and projects >=2; In Progress if completion >=60; otherwise Needs Attention.
"""
print("*" * 10 + " Question-30: Online course completion certificates " + "*" * 10)
print(question_30)
print("-*" * 60)

course_data = [
    {"name": "Anu", "progress": (92, 3), "modules": ["Python", "SQL"]},
    {"name": "Ravi", "progress": (68, 1), "modules": ["Python"]},
    {"name": "Meena", "progress": (100, 4), "modules": ["Python", "SQL", "AI"]}
]

name_to_status = {}
for student in course_data:
    name = student["name"]
    completion_percent, projects = student["progress"]
    if completion_percent >= 90 and projects >= 2:
        status = "Certificate Ready"
    elif completion_percent >= 60:
        status = "In Progress"
    else:
        status = "Needs Attention"
    name_to_status[name] = status
    print(f"Student Name: {name}\n Completion Percent: {completion_percent}\n Projects: {projects}\n Status: {status}")
    print(" -" * 20)

print(f"Name to Status Mapping: {name_to_status}")
print("=" * 60)
