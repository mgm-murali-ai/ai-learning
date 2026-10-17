
question_01 = '''
Question-01. Library borrower record
{"member":"Anu","books":["Python 101","Data Basics"],"due_days":(3,8),"membership":"Active"}
Task: Print member, first borrowed book and second due-day value; append 'AI Basics' to books; print updated book count.
'''
print(question_01)
print("*"*10 + " Library Borrower Record " + "*"*10)    
Library_data = {"member":"Anu","books":["Python 101","Data Basics"],"due_days":(3,8),"membership":"Active"}
print(f"Member: {Library_data['member']}")
print(f"First borrowed book: {Library_data['books'][0]}")
print(f"Second due-day value: {Library_data['due_days'][1]}")
Library_data['books'].append('AI Basics')
print(f"Updated book count: {len(Library_data['books'])}")
# Print all above values in a single line
# print(f"Member: {Library_data['member']}\nFirst borrowed book: {Library_data['books'][0]}\nSecond due-day value: {Library_data['due_days'][1]}")
print("=" * 50)
question_02 = '''
Question-02. Food order summary
Structure: List of dictionaries with item tuple
Starter data
[{"item":"Dosa","order":(80,2)},{"item":"Idli","order":(50,3)},{"item":"Coffee","order":(30,2)}]
Task: Print each item's name and line total; calculate total bill for the order.
'''
print(question_02)
print("*"*10 + " Food Order Summary " + "*"*10)
food_order = [{"item":"Dosa","order":(80,2)},{"item":"Idli","order":(50,3)},{"item":"Coffee","order":(30,2)}]
total_bill = 0
for order in food_order:
    item_name = order['item']
    # print(f"Item: {item_name}")
    order_details = order['order']
    price = order_details[0]
    quantity = order_details[1]
    line_total = price * quantity
    total_bill += line_total
    print(f"Item: {item_name}\n Line Total: {line_total}")
    print(" Total Bill: ", total_bill)
    print(" -" * 10)

print(f"Total Bill: {total_bill}")
print("=" * 50)
question_03 = '''
Question-03. Classroom attendance
Structure: Dictionary with a list of attendance flags
Starter data
{"Rahul":[1,1,0,1,1],"Anu":[1,1,1,1,1],"Sai":[1,0,0,1,0]}
Task: Calculate attendance percentage for each student using sum() and len(); print Eligible for >=75%, Warning for >=50%, otherwise Low Attendance.
'''
print(question_03)
print("*"*10 + " Attendance Report " + "*"*10)
classroom_attendance = {"Rahul":[1,1,0,1,1],"Anu":[1,1,1,1,1],"Sai":[1,0,0,1,0]}
for student in classroom_attendance.items():
    student_name = student[0]
    attendance_flags = student[1]
    attendance_percentage = (sum(attendance_flags) / len(attendance_flags)) * 100
    if attendance_percentage >= 75:
        print(f"Student: {student_name}")
        print(f"  Attendance Flags: {attendance_flags}")
        print(f"  Attendance Percentage: {attendance_percentage}%")
        print("  Status: Eligible")
    elif attendance_percentage >= 50:
        print(f"Student: {student_name}")
        print(f"  Attendance Flags: {attendance_flags}")
        print(f"  Attendance Percentage: {attendance_percentage:.2f}%")
        print("  Status: Warning")
    else:
        print(f"Student: {student_name}")
        print(f"  Attendance Flags: {attendance_flags}")
        print(f"  Attendance Percentage: {attendance_percentage:.2f}%")
        print("  Status: Low Attendance")

    print("  -" * 12)
print("=" * 50)
question_04 = '''
Question-04. Cinema seat booking
Structure: Dictionary with a set and tuple
Starter data
{"movie":"Space Quest","booked":{"A1","A2","B3"},"requested":("A3","A2","B4")}
Task: Use one loop over requested seats. Print Already Booked if seat exists in booked set; otherwise print Available and add seat to booked set. Print final booked set.
'''
print(question_04)
print("*"*10 + " Cinema Seat Booking " + "*"*10)
cinema_seats = {"movie":"Space Quest","booked":{"A1","A2","B3"},"requested":("A3","A2","B4")}

print(f"Movie: {cinema_seats['movie']}")
for seat in cinema_seats["requested"]:
    if seat in cinema_seats["booked"]:
        print(f"  Seat {seat}: Already Booked")
    else:
        print(f"  Seat {seat}: Available")
        cinema_seats["booked"].add(seat)

print(f"Final Booked Seats: {cinema_seats['booked']}")
print("=" * 50)
question_05 = '''
Question-05. Mobile plan comparison
Structure: List of dictionaries with a tuple
Starter data
[{"plan":"Basic","details":(199,2)},{"plan":"Plus","details":(399,6)},{"plan":"Max","details":(699,12)}]
Task: Each tuple is (price, data_GB). Print Affordable if price <=399 and data >=2; High Data if data >=10; otherwise Standard.
'''
print(question_05)
print("*"*10 + " Mobile Plan Comparison " + "*"*10)
mobile_plans = [{"plan":"Basic","details":(199,2)},{"plan":"Plus","details":(399,6)},{"plan":"Max","details":(699,12)}]
for plan in mobile_plans:
    plan_name = plan['plan']
    plan_details = plan['details']
    plan_price = plan_details[0]
    plan_data_GB = plan_details[1]
    if plan_price <= 399 and plan_data_GB >= 2:
        status = "Affordable"
    elif plan_data_GB >= 10:
        status = "High Data"
    else:
        status = "Standard"
    
    print(f"Plan: {plan_name}\n Price: {plan_price}\n Data: {plan_data_GB}GB\n Status: {status}")
    print(" -" * 10)
print("=" * 50)
question_06 = '''
Question-06. Student skill badge checker
Structure: Dictionary containing a set
Starter data
{"Rahul":{"Python","SQL"},"Anu":{"Python","GenAI","RAG"},"Sai":{"Excel"}}
Task: Print AI Ready if GenAI or RAG is present; Python Learner if Python is present; otherwise Beginner. Use one loop.
'''
print(question_06)
print("*"*10 + " Student Skill Badge Checker " + "*"*10)
student_skills = {"Rahul":{"Python","SQL"},"Anu":{"Python","GenAI","RAG"},"Sai":{"Excel"}} 
for student, skills in student_skills.items():
    if "GenAI" in skills or "RAG" in skills:
        badge = "AI Ready"
    elif "Python" in skills:
        badge = "Python Learner"
    else:
        badge = "Beginner"
    
    print(f"Student: {student}\n Skills: {skills}\n Badge: {badge}")
    print(" -" * 10)
print("=" * 50)
question_07 = '''
Question-07. Travel booking price check
Structure: List of dictionaries with tuple
Starter data
[{"guest":"Asha","booking":(2,3500)},{"guest":"Ravi","booking":(4,5000)},{"guest":"Meena","booking":(1,2500)}]
Task: Each booking tuple is (nights, nightly_price). Calculate total for each guest; apply 10% discount if nights >=3, otherwise no discount; print payable.
'''
print(question_07)
print("*"*10 + " Travel Booking Price Check " + "*"*10)
travel_bookings = [{"guest":"Asha","booking":(2,3500)},{"guest":"Ravi","booking":(4,5000)},{"guest":"Meena","booking":(1,2500)}]
for booking in travel_bookings:
    guest_name = booking['guest']
    booking_details = booking['booking']
    num_of_nights = booking_details[0]
    price_per_night = booking_details[1]
    total_price = num_of_nights * price_per_night
    if num_of_nights >= 3:
        discount = total_price * 0.10
    else:
        discount = 0
    payable_amount = total_price - discount
    
    print(f"Guest: {guest_name}\n Nights: {num_of_nights}\n Nightly Price: {price_per_night}\n Total Price: {total_price}\n Discount: {discount}\n Payable Amount: {payable_amount}")
    print(f" Payable Amount for {guest_name}: {payable_amount}")
    print(" -" * 10)
print("=" * 50)
question_08 = '''
Question-08. Student profile dashboard
Structure: Dictionary containing strings, a list, tuple and set
Starter data
student = {"name": "Rahul", "email": "rahul@gmail.com", "courses": ["Python", "SQL", "GenAI"], "marks": (85, 92, 78), "skills": {"Python", "SQL", "HTML"}, "fees_paid": 11000}
Task: Print name, email, second course and last mark; add Agentic AI to courses and FastAPI to skills; calculate average marks; classify Excellent (>=85), Good (>=60), otherwise Needs Improvement; classify fee as Full, Partial or Pending against ₹22,000.
'''
print(question_08)
print("*"*10 + " Student Profile Dashboard " + "*"*10)
student_data = {"name": "Rahul", "email": "rahul@gmail.com", "courses": ["Python", "SQL", "GenAI"], "marks": (85, 92, 78), "skills": {"Python", "SQL", "HTML"}, "fees_paid": 11000}
student_courses = student_data['courses']
student_skills = student_data['skills']
student_marks = student_data['marks']
print(f"Name: {student_data['name']}")
print(f"Email: {student_data['email']}")
print(f"Second Course: {student_courses[1]}")
print(f"Last Mark: {student_marks[-1]}")
student_courses.append("Agentic AI")
student_skills.add("FastAPI")
average_marks = sum(student_marks) / len(student_marks)
if average_marks >= 85:
    performance = "Excellent"
elif average_marks >= 60:
    performance = "Good"
else:
    performance = "Needs Improvement"

print(f"Average Marks: {average_marks}")
print(f"Performance: {performance}")
print(f"Courses after addition: {student_courses}")
print(f"Skills after addition: {student_skills}")
fee_paid = student_data['fees_paid']
if fee_paid == 22000:
    fee_status = "Full"
elif ((fee_paid > 0) and (fee_paid < 22000)):
    fee_status = "Partial"
else:
    fee_status = "Pending"

print(f"Fee Status: {fee_status}")
print("=" * 50)
question_09 = '''
Question-09. Product catalog labels
Structure: Dictionary of product dictionaries
Starter data
{"P01":{"name":"Laptop","price":55000,"tags":{"electronics","premium"}},"P02":{"name":"Mouse","price":700,"tags":{"accessory"}},"P03":{"name":"Monitor","price":12000,"tags":{"electronics"}}}
Task: Print Premium if premium is in tags or price >=50000; Electronics if electronics in tags; otherwise General.
'''
print(question_09)
print("*"*10 + " Product Catalog Labels " + "*"*10)
product_catalog = {"P01":{"name":"Laptop","price":55000,"tags":{"electronics","premium"}},"P02":{"name":"Mouse","price":700,"tags":{"accessory"}},"P03":{"name":"Monitor","price":12000,"tags":{"electronics"}}}
for product_id, product_info in product_catalog.items():
    product_name = product_info['name']
    product_price = product_info['price']
    product_tags = product_info['tags']
    
    if ("premium" in product_tags or product_price >= 50000):
        label = "Premium"
    elif "electronics" in product_tags:
        label = "Electronics"
    else:
        label = "General"
    
    print(f"Product ID: {product_id}\n Name: {product_name}\n Price: {product_price}\n Tags: {product_tags}\n Label: {label}")
    print(" -" * 10)
print("=" * 50)
question_10 = '''
Question-10. Restaurant order preparation
Structure: List of dictionaries containing lists
Starter data
[{"table":1,"items":["Dosa","Tea"],"minutes":12},{"table":2,"items":["Biryani","Juice","Water"],"minutes":30},{"table":3,"items":["Idli"],"minutes":8}]
Task: Print table number, item count and urgency: Fast (<10 minutes), Normal (10–20), Delayed (>20).
'''
print(question_10)
print("*"*10 + " Restaurant Order Preparation " + "*"*10)
restaurant_orders = [{"table":1,"items":["Dosa","Tea"],"minutes":12},{"table":2,"items":["Biryani","Juice","Water"],"minutes":30},{"table":3,"items":["Idli"],"minutes":8}]
for order in restaurant_orders:
    table_number = order['table']
    item_count = len(order['items'])
    preparation_time = order['minutes']
    
    if preparation_time < 10:
        urgency = "Fast"
    elif 10 <= preparation_time <= 20:
        urgency = "Normal"
    else:
        urgency = "Delayed"
    
    print(f"Table Number: {table_number}\n Item Count: {item_count}\n Preparation Time: {preparation_time} minutes\n Urgency: {urgency}")
    print(" -" * 10)
print("=" * 50)