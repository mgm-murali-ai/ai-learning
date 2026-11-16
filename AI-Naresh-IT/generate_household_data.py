"""Generate a dummy household dataset as a CSV file (household_data.csv).

Columns:
    Mthly_HH_Income          monthly household income
    Mthly_HH_Expense         monthly household expense
    No_of_Family_Members     number of family members
    Emi_or_Rent_Amt          EMI or rent paid every month (0 = none)
    Annual_HH_Income         income for the whole year
    Highest Qualified Member education of the most qualified member
    No_of_Earning_Members    members who earn

The rows are sorted by monthly income (low to high).
Some "Under-Graduate" rows are written as "Under Graduate" on purpose, so there is a messy
label to clean (set dirty=0 to turn this off).

Usage:
    python generate_household_data.py                 # 50 rows
    python generate_household_data.py 200             # 200 rows
    python generate_household_data.py 200 7 0         # 200 rows, seed 7, no messy labels
"""
import csv
import random
import sys

HEADERS = [
    "Mthly_HH_Income", "Mthly_HH_Expense", "No_of_Family_Members", "Emi_or_Rent_Amt",
    "Annual_HH_Income", "Highest Qualified Member", "No_of_Earning_Members",
]
QUALIFICATIONS = ["Illiterate", "Under-Graduate", "Graduate", "Post-Graduate"]
QUALIFICATION_WEIGHTS = [2, 4, 3, 1]


def make_rows(count, seed=42, dirty=True):
    rng = random.Random(seed)
    incomes = sorted(rng.randrange(5000, 60001, 500) for _ in range(count))
    rows = []
    for income in incomes:
        members = rng.randint(1, 6)
        earning = rng.randint(1, min(2, members))
        expense = round(income * rng.uniform(0.25, 1.3) / 500) * 500
        emi_rent = 0 if rng.random() < 0.55 else rng.randrange(2000, 36000, 1000)
        annual = 12 * round(income * rng.uniform(0.8, 1.2))
        qualification = rng.choices(QUALIFICATIONS, QUALIFICATION_WEIGHTS)[0]
        rows.append([income, expense, members, emi_rent, annual, qualification, earning])
    if dirty:
        # write about 1 in 6 "Under-Graduate" labels as "Under Graduate" (at least one)
        under = [i for i, r in enumerate(rows) if r[5] == "Under-Graduate"]
        for i in rng.sample(under, max(1, len(under) // 6)):
            rows[i][5] = "Under Graduate"
    return rows


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 42
    dirty = bool(int(sys.argv[3])) if len(sys.argv) > 3 else True

    with open("household_data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        writer.writerows(make_rows(count, seed, dirty))

    print(f"Wrote {count} rows to household_data.csv")
