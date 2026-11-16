"""Generate dummy country data (CountryName, CountryCode, BirthRate, InternetUsers, IncomeGroup).

Every row is a real country with its real code. Names are never numbered or changed.
If you ask for more rows than there are countries, some countries repeat (duplicate rows
with the same name and code, but different BirthRate and InternetUsers values).

Usage:
    python generate_dummy_data.py                  # all countries in the list -> countries_dummy.xlsx
    python generate_dummy_data.py 50               # 50 randomly chosen countries
    python generate_dummy_data.py 500              # 500 rows (every country once, the rest repeated)
    python generate_dummy_data.py 100 0.05         # 100 rows, ~5% of cells left empty (for cleaning practice)
    python generate_dummy_data.py 195 0 10         # 195 rows, no empty cells, 10 outliers -> countries_outliers.xlsx

Needs the openpyxl package:  pip install openpyxl
"""
import random
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter

H, UM, LM, L = "High income", "Upper middle income", "Lower middle income", "Low income"

COUNTRIES = [
    ("Aruba", "ABW", H), ("Afghanistan", "AFG", L), ("Angola", "AGO", UM), ("Albania", "ALB", UM),
    ("United Arab Emirates", "ARE", H), ("Argentina", "ARG", H), ("Armenia", "ARM", LM),
    ("Antigua and Barbuda", "ATG", H), ("Australia", "AUS", H), ("Austria", "AUT", H),
    ("Azerbaijan", "AZE", UM), ("Burundi", "BDI", L), ("Belgium", "BEL", H), ("Benin", "BEN", L),
    ("Burkina Faso", "BFA", L), ("Bangladesh", "BGD", LM), ("Bulgaria", "BGR", UM),
    ("Bahrain", "BHR", H), ("Bahamas, The", "BHS", H), ("Bosnia and Herzegovina", "BIH", UM),
    ("Belarus", "BLR", UM), ("Belize", "BLZ", UM), ("Bermuda", "BMU", H), ("Bolivia", "BOL", LM),
    ("Brazil", "BRA", UM), ("Barbados", "BRB", H), ("Brunei Darussalam", "BRN", H),
    ("Bhutan", "BTN", LM), ("Botswana", "BWA", UM), ("Central African Republic", "CAF", L),
    ("Canada", "CAN", H), ("Switzerland", "CHE", H), ("Chile", "CHL", H), ("China", "CHN", UM),
    ("Cote d'Ivoire", "CIV", LM), ("Cameroon", "CMR", LM), ("Congo, Rep.", "COG", LM),
    ("Colombia", "COL", UM), ("Comoros", "COM", LM), ("Cabo Verde", "CPV", LM),
    ("Costa Rica", "CRI", UM), ("Cuba", "CUB", UM), ("Cayman Islands", "CYM", H),
    ("Cyprus", "CYP", H), ("Czech Republic", "CZE", H), ("Germany", "DEU", H),
    ("Djibouti", "DJI", LM), ("Denmark", "DNK", H), ("Dominican Republic", "DOM", UM),
    ("Algeria", "DZA", LM), ("Ecuador", "ECU", UM), ("Egypt, Arab Rep.", "EGY", LM),
    ("Eritrea", "ERI", L), ("Spain", "ESP", H), ("Estonia", "EST", H), ("Ethiopia", "ETH", L),
    ("Finland", "FIN", H), ("Fiji", "FJI", UM), ("France", "FRA", H),
    ("Micronesia, Fed. Sts.", "FSM", LM), ("Gabon", "GAB", UM), ("United Kingdom", "GBR", H),
    ("Georgia", "GEO", UM), ("Ghana", "GHA", LM), ("Guinea", "GIN", L), ("Gambia, The", "GMB", L),
    ("Guinea-Bissau", "GNB", L), ("Equatorial Guinea", "GNQ", UM), ("Greece", "GRC", H),
    ("Grenada", "GRD", UM), ("Greenland", "GRL", H), ("Guatemala", "GTM", UM), ("Guam", "GUM", H),
    ("Guyana", "GUY", UM), ("Hong Kong SAR, China", "HKG", H), ("Honduras", "HND", LM),
    ("Croatia", "HRV", H), ("Haiti", "HTI", LM), ("Hungary", "HUN", H), ("Indonesia", "IDN", UM),
    ("India", "IND", LM), ("Ireland", "IRL", H), ("Iran, Islamic Rep.", "IRN", UM),
    ("Iraq", "IRQ", UM), ("Iceland", "ISL", H), ("Israel", "ISR", H), ("Italy", "ITA", H),
    ("Jamaica", "JAM", UM), ("Jordan", "JOR", UM), ("Japan", "JPN", H), ("Kazakhstan", "KAZ", UM),
    ("Kenya", "KEN", LM), ("Kyrgyz Republic", "KGZ", LM), ("Cambodia", "KHM", LM),
    ("Kiribati", "KIR", LM), ("Korea, Rep.", "KOR", H), ("Kuwait", "KWT", H), ("Lao PDR", "LAO", LM),
    ("Lebanon", "LBN", UM), ("Liberia", "LBR", L), ("Libya", "LBY", UM), ("St. Lucia", "LCA", UM),
    ("Liechtenstein", "LIE", H), ("Sri Lanka", "LKA", LM), ("Lesotho", "LSO", LM),
    ("Lithuania", "LTU", H), ("Luxembourg", "LUX", H), ("Latvia", "LVA", H),
    ("Macao SAR, China", "MAC", H), ("Morocco", "MAR", LM), ("Moldova", "MDA", UM),
    ("Madagascar", "MDG", L), ("Maldives", "MDV", UM), ("Mexico", "MEX", UM),
    ("Macedonia, FYR", "MKD", UM), ("Mali", "MLI", L), ("Malta", "MLT", H), ("Myanmar", "MMR", LM),
    ("Montenegro", "MNE", UM), ("Mongolia", "MNG", LM), ("Mozambique", "MOZ", L),
    ("Mauritania", "MRT", LM), ("Mauritius", "MUS", UM), ("Malawi", "MWI", L), ("Malaysia", "MYS", UM),
    ("Namibia", "NAM", UM), ("New Caledonia", "NCL", H), ("Niger", "NER", L), ("Nigeria", "NGA", LM),
    ("Nicaragua", "NIC", LM), ("Netherlands", "NLD", H), ("Norway", "NOR", H), ("Nepal", "NPL", LM),
    ("New Zealand", "NZL", H), ("Oman", "OMN", H), ("Pakistan", "PAK", LM), ("Panama", "PAN", H),
    ("Peru", "PER", UM), ("Philippines", "PHL", LM), ("Papua New Guinea", "PNG", LM),
    ("Poland", "POL", H), ("Puerto Rico", "PRI", H), ("Korea, Dem. Rep.", "PRK", L),
    ("Portugal", "PRT", H), ("Paraguay", "PRY", UM), ("West Bank and Gaza", "PSE", LM),
    ("French Polynesia", "PYF", H), ("Qatar", "QAT", H), ("Romania", "ROU", H),
    ("Russian Federation", "RUS", UM), ("Rwanda", "RWA", L), ("Saudi Arabia", "SAU", H),
    ("Sudan", "SDN", L), ("Senegal", "SEN", LM), ("Singapore", "SGP", H),
    ("Solomon Islands", "SLB", LM), ("Sierra Leone", "SLE", L), ("El Salvador", "SLV", LM),
    ("Somalia", "SOM", L), ("Serbia", "SRB", UM), ("South Sudan", "SSD", L),
    ("Sao Tome and Principe", "STP", LM), ("Suriname", "SUR", UM), ("Slovak Republic", "SVK", H),
    ("Slovenia", "SVN", H), ("Sweden", "SWE", H), ("Swaziland", "SWZ", LM), ("Seychelles", "SYC", H),
    ("Syrian Arab Republic", "SYR", L), ("Chad", "TCD", L), ("Togo", "TGO", L), ("Thailand", "THA", UM),
    ("Tajikistan", "TJK", LM), ("Turkmenistan", "TKM", UM), ("Timor-Leste", "TLS", LM),
    ("Tonga", "TON", UM), ("Trinidad and Tobago", "TTO", H), ("Tunisia", "TUN", LM),
    ("Turkey", "TUR", UM), ("Tanzania", "TZA", LM), ("Uganda", "UGA", L), ("Ukraine", "UKR", LM),
    ("Uruguay", "URY", H), ("United States", "USA", H), ("Uzbekistan", "UZB", LM),
    ("St. Vincent and the Grenadines", "VCT", UM), ("Venezuela, RB", "VEN", UM),
    ("Virgin Islands (U.S.)", "VIR", H), ("Vietnam", "VNM", LM), ("Vanuatu", "VUT", LM),
    ("Samoa", "WSM", UM), ("Yemen, Rep.", "YEM", L), ("South Africa", "ZAF", UM),
    ("Congo, Dem. Rep.", "COD", L), ("Zambia", "ZMB", LM), ("Zimbabwe", "ZWE", LM),
]

# income group -> (birth rate range per 1000 people, internet users % range)
RANGES = {
    H: ((8.0, 18.0), (60.0, 98.0)),
    UM: ((10.0, 25.0), (30.0, 75.0)),
    LM: ((15.0, 35.0), (8.0, 50.0)),
    L: ((30.0, 50.0), (1.0, 20.0)),
}


def make_rows(count, seed=42):
    rng = random.Random(seed)
    if count <= len(COUNTRIES):
        chosen = rng.sample(COUNTRIES, count)
    else:
        # use every country once, then repeat random countries (same name and code) for the extra rows
        chosen = COUNTRIES + rng.choices(COUNTRIES, k=count - len(COUNTRIES))
    rows = []
    for name, code, group in chosen:
        (b_lo, b_hi), (n_lo, n_hi) = RANGES[group]
        rows.append({
            "CountryName": name,
            "CountryCode": code,
            "BirthRate": round(rng.uniform(b_lo, b_hi), 3),
            "InternetUsers": round(rng.uniform(n_lo, n_hi), 2),
            "IncomeGroup": group,
        })
    rng.shuffle(rows)                        # random order, not sorted by code
    return rows


def blank_some(rows, rate, seed=7):
    rng = random.Random(seed)
    for row in rows:
        for col in ("BirthRate", "InternetUsers", "IncomeGroup"):
            if rng.random() < rate:
                row[col] = None


def add_outliers(rows, how_many, seed=11):
    """Replace one value in `how_many` random rows with an extreme value (an outlier).

    BirthRate outliers are 70 to 150 (normal data is about 8 to 50).
    InternetUsers outliers are 150 to 500 (it is a percentage, so anything above 100 is impossible).
    """
    rng = random.Random(seed)
    changed = []
    for row in rng.sample(rows, how_many):
        col = rng.choice(["BirthRate", "InternetUsers"])
        old = row[col]
        row[col] = round(rng.uniform(70, 150), 3) if col == "BirthRate" else round(rng.uniform(150, 500), 2)
        changed.append((row["CountryName"], col, old, row[col]))
    return changed


if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else len(COUNTRIES)
    missing = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
    outliers = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    data = make_rows(count)
    if missing > 0:
        blank_some(data, missing)
    output_file = "countries_dummy.xlsx"
    if outliers > 0:
        output_file = "countries_outliers.xlsx"      # a separate file, so the clean file is not overwritten
        for name, col, old, new in add_outliers(data, outliers):
            print(f"  outlier: {name} -> {col}: {old} changed to {new}")
    wb = Workbook()
    ws = wb.active
    ws.title = "Countries"
    headers = list(data[0])
    ws.append(headers)
    for row in data:
        ws.append([row[h] for h in headers])

    center = Alignment(horizontal="center")
    for cell in ws[1]:
        cell.font = Font(bold=True)
    for r in ws.iter_rows(min_row=1):
        for cell in r:
            cell.alignment = center
    ws.auto_filter.ref = ws.dimensions       # filter drop-downs on the header row, like the sample
    ws.freeze_panes = "A2"
    for i, h in enumerate(headers, start=1):
        width = max(len(h), *(len(str(row[h])) for row in data if row[h] is not None)) + 4
        ws.column_dimensions[get_column_letter(i)].width = width

    wb.save(output_file)
    print(f"Wrote {len(data)} rows to {output_file}")
