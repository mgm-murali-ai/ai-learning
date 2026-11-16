print("*" * 72)
print("*" * 15 + " SECTION A  |  Core business functions (1–8) " + "*" * 15)
print("*" * 72)
print(" ")
print("*" * 10 + "Question-01. Student Fee Reconciliation " + "*" * 10)
question_01 = '''Required function: reconcile_fees(payments, fees)
Scenario & task: Return a dictionary of remaining balances (never negative). Assume every student ID in payments exists in fees.
Sample input
payments = {"ST101": 11000, "ST102": 22000, "ST103": 0}
fees = {"ST101": 22000, "ST102": 22000, "ST103": 20000}
Expected return value
{"ST101": 11000, "ST102": 0, "ST103": 20000}
'''
print(question_01)
print("*" * 10 + " Question-01: Student Fee Reconciliation " + "*" * 10)
# print(" " * 5 + "**Answer**")
def reconcile_fees(payments, fees):
    remaining_balances = {}
    for student_id, fee in fees.items():
        stdnt_payment = payments[student_id]
        student_fee = fee
        # print(f"Student ID: {student_id}, Payment: {stdnt_payment}, Fee: {student_fee}")
        if student_fee - stdnt_payment <= 0:
            remaining_balances[student_id] = 0
        else:
            remaining_balances[student_id] = student_fee - stdnt_payment
    return remaining_balances
# Test the function
payments = {"ST101": 11000, "ST102": 22000, "ST103": 0}
fees = {"ST101": 22000, "ST102": 22000, "ST103": 20000}
print("Pending balances:", reconcile_fees(payments, fees))
print("-" * 72)