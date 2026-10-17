import pyfiglet
from rich import print, box
from rich.panel import Panel
from rich.align import Align

text = "\n".join(
    l
    for l in pyfiglet.figlet_format("Part-1", font="xhelvbi").splitlines()
    if l.strip()
)
print(
    Panel(
        Align.center(f"[green]{text}[/green]"),
        box=box.DOUBLE_EDGE,
        border_style="green",
        width=50,
        padding=(1, 2),
    )
)

print("=" * 65)
names = ["ravi", "ANU", "kiran", "sai"]
# convert to title case
# names_title_case = [name.title() for name in names]
for name in names:
    print(f"Before title case: {name} -> After title case: {name.title()}")
print("=" * 65)


## A stationery shop records sales for five days. Calculate total sales using a for loop and an accumulator.
sales = [200, 350, 150, 400, 300]
total_sales = 0
for sale in sales:
    total_sales += sale
print(f"Total sales for the week: {total_sales}")
print("=" * 65)

## A class needs to display marks of students who passed (40 or above).
marks = [32, 48, 75, 39, 61]
students_passed = []
for mark in marks:
    if mark >= 40:
        students_passed.append(mark)
print(f"Students who passed: {students_passed}")
print("=" * 65)


S = "Hyderabad is capital city"
length = len(S)
print(f"Length of the string: {length}")
# S[:9]
# S[10:]
# S[-4:]
print(f"First 9 characters: {S[:9]}")
print(f"Characters from index 10 to 16: {S[10:]}")
print(f"Last 4 characters: {S[-4:]}")
print("=" * 65)


### A weather app labels each reading as Hot (>=35), Warm (>=25), or Cool (otherwise).
temps = [20, 29, 38, 24, 35]
for temp in temps:
    if temp >= 35:
        print(f"{temp}°C -> Hot")
    elif temp >= 25:
        print(f"{temp}°C -> Warm")
    else:
        print(f"{temp}°C -> Cool")
print("=" * 65)


## A class roster contains three names. Add "Meena" using append(), then print the updated list.
## Expected result:  ["Ram", "Anu", "Kiran", "Meena"]
# print(f"Before adding Meena: {students}")
students = ["Ram", "Anu", "Kiran"]
students.append("Meena")
print(f"After adding Meena: {students}")
print("=" * 65)

## Two workshop batches are merged. Use extend() and print the combined participant list.
batch_a = ["Ravi", "Sai"]
batch_b = ["Anu", "Meena"]
batch_a.extend(batch_b)
print(f"Final result: {batch_a}")
print("=" * 65)

question_p1_07 = """A trainer forgot "Operators" in the course order. Insert it between "Variables" and "Strings".
Given data:  topics = ["Variables", "Strings", "Lists"]
Expected result:  ["Variables", "Operators", "Strings", "Lists"]
"""
topics = ["Variables", "Strings", "Lists"]
topics.insert(1, "Operators")
print(f"Final result: {topics}")
print("=" * 65)

question_p1_08 = """A shop stores six order IDs. Print the last three IDs using slicing.
Given data:  orders = [101, 102, 103, 104, 105, 106]
Expected result:  [104, 105, 106]
"""
print(f"Question: [bold red]{question_p1_08}[/bold red]")
print("[cyan]=[/cyan]" * 65)
orders = [101, 102, 103, 104, 105, 106]
print(f"Last three order IDs: {orders[3:]}")
print("=" * 65)

question_p1_09 = """A school stores a fixed tuple of courses. Use a for loop to print each course and print the first two courses using slicing.
Given data:  courses = ("Python", "SQL", "AI", "ML")
Expected result:  First two: ("Python", "SQL")
"""
print(f"Question: [bold red]{question_p1_09}[/bold red]")
print("[cyan]=[/cyan]" * 65)
courses = ("Python", "SQL", "AI", "ML")
for course in courses:
    print(f"Course: {course}")
print(f"First two courses: {courses[:2]}")
print("=" * 65)
####################
question_p1_10 = """A store classifies each price: Budget if below 500, Standard if 500–1500 inclusive, Premium otherwise.
Given data:  prices = [250, 750, 1500, 2200]
Expected result:  Budget, Standard, Standard, Premium  
"""
print(f"Question: [bold red]{question_p1_10}[/bold red]")

prices = [250, 750, 1500, 2200]
print("Answer:")
for price in prices:
    if price < 500:
        print(f"{price} -> Budget")
    elif price <= 1500:
        print(f"{price} -> Standard")
    else:
        print(f"{price} -> Premium")

print("[cyan]=[/cyan]" * 65)

text = "\n".join(
    l
    for l in pyfiglet.figlet_format("Part-2", font="xhelvbi").splitlines()
    if l.strip()
)

print(
    Panel(
        Align.center(f"[green]{text}[/green]"),
        box=box.DOUBLE_EDGE,
        border_style="green",
        width=50,
        padding=(1, 2),
    )
)
print("[cyan]=[/cyan]" * 65)


question_p2_1 = """A training institute allows certificates only for attendance between 75 and 100 inclusive. Put eligible values in a new list; put all others in another list.
Given data:  attendance = [92, 68, 75, 100, 54, 110]
Expected result:  Eligible: [92, 75, 100]; Others: [68, 54, 110]
"""
print(f"Question: [bold red]{question_p2_1}[/bold red]")

attendance = [92, 68, 75, 100, 54, 110]
eligible = []
others = []
for att in attendance:
    if (75 <= att) and (att <= 100):
        eligible.append(att)
    else:
        others.append(att)

print(f"[green bold]Answer:[/green bold]\n Eligible: {eligible}; Others: {others}")
print("[cyan]=[/cyan]" * 65)
