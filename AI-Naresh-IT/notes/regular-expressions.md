# Regular Expressions in Python

## What is a regular expression?

- A regular expression (**regex**) is a **pattern** that describes a piece of text.
- You use it to **find**, **extract**, **replace** or **split** text, without writing long loops and `if` conditions.
- Example: the pattern `\d+` means "one or more digits". It finds `12`, `450` and `3` in `"Order 12, price 450 and qty 3"`.
- Python has a built-in module for it: `re`.

```python
import re
```

Where it is useful in data work (EDA):

- Cleaning messy text, for example removing the symbols from `5^00#0` to get `5000`.
- Extracting a number from text, for example `34` from `34 years`.
- Checking a format, for example an email, a phone number or a date.

## Raw strings: always write the pattern as `r"..."`

In a normal string, `\n` is a new line and `\b` is a backspace. A regex uses the backslash for its own codes (`\d`, `\w`, `\b`). Put an `r` before the quotes (a **raw string**) so Python leaves the backslash alone.

```python
re.findall(r"\d+", "a12")      # correct: ['12']
```

## The main functions of `re`

| Function               | What it does                                         | Returns                      |
| ---------------------- | ---------------------------------------------------- | ---------------------------- |
| `re.search(p, s)`    | Finds the **first** match anywhere in the text | A match object, or `None`  |
| `re.match(p, s)`     | Matches only at the **start** of the text      | A match object, or `None`  |
| `re.fullmatch(p, s)` | The **whole** text must match                  | A match object, or `None`  |
| `re.findall(p, s)`   | Finds **all** matches                          | A list of strings            |
| `re.finditer(p, s)`  | Finds all matches, with their positions              | An iterator of match objects |
| `re.sub(p, new, s)`  | **Replaces** the matches                       | A new string                 |
| `re.split(p, s)`     | **Splits** the text at the matches             | A list of strings            |
| `re.compile(p)`      | Saves a pattern to use again                         | A pattern object             |

### re.search()

```python
s = "Python 3.12 is great"

m = re.search(r"\d+\.\d+", s)
print(m.group())     # 3.12   (the matched text)
print(m.span())      # (7, 11) (start and end position)
```

- `m.group()` gives the text that matched. If nothing matches, `re.search()` returns `None`, so check before you use it:

```python
m = re.search(r"\d+", "no numbers")
if m:
    print(m.group())
else:
    print("no match")        # no match
```

### re.match() and re.fullmatch()

```python
s = "Python 3.12 is great"

print(re.match(r"Python", s))     # <re.Match object; span=(0, 6), match='Python'>   (it starts with Python)
print(re.match(r"3.12", s))       # None   (3.12 is not at the start)

print(re.fullmatch(r"\d+", "12345"))   # <re.Match object; span=(0, 5), match='12345'>
print(re.fullmatch(r"\d+", "123a"))    # None   (the whole text must be digits)
```

|                | `search`        | `match`              | `fullmatch`       |
| -------------- | ----------------- | ---------------------- | ------------------- |
| Where it looks | Anywhere          | Start only             | The whole text      |
| Use for        | Finding something | Checking the beginning | Validating a format |

### re.findall() and re.finditer()

```python
print(re.findall(r"\d+", "Order 12, price 450 and qty 3"))
# ['12', '450', '3']

for m in re.finditer(r"\d+", "Order 12, price 450"):
    print(m.group(), m.start(), m.end())
# 12 6 8
# 450 16 19
```

### re.sub(): replace

```python
print(re.sub(r"\d", "#", "a1b22"))          # a#b##      (every digit becomes #)
print(re.sub(r"\s+", " ", "a   b \n c"))    # a b c      (many spaces and new lines become one space)
```

The replacement can also be a function. It gets each match and returns the new text:

```python
print(re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a5 b10"))     # a10 b20
```

### re.split()

```python
print(re.split(r"[,;]\s*", "a, b;c,  d"))     # ['a', 'b', 'c', 'd']
```

The text is split at every comma or semicolon, with any spaces after it.

### re.compile(): use a pattern many times

```python
pat = re.compile(r"\d+")

print(pat.findall("a1 b22 c333"))     # ['1', '22', '333']
print(pat.sub("#", "a1 b22"))         # a# b#
```

## Building a pattern

### 1. Ordinary characters and the dot

Letters and digits match themselves. A **dot** `.` matches any one character (except a new line). To match a real dot, write `\.`.

```python
print(re.findall(r"a.c", "abc a.c a\nc"))     # ['abc', 'a.c']   (the dot does not match the new line)
print(re.findall(r"a\.c", "abc a.c"))         # ['a.c']          (only a real dot)
print(re.findall(r"\$\d+\.\d{2}", "Total $45.50 and $3.00"))     # ['$45.50', '$3.00']
```

### 2. Character classes

| Pattern      | Matches                                                                        |
| ------------ | ------------------------------------------------------------------------------ |
| `\d`       | A digit `0-9`                                                                |
| `\D`       | Anything that is **not** a digit                                         |
| `\w`       | A letter, a digit or `_`                                                     |
| `\W`       | Anything that is not a letter, digit or `_`                                  |
| `\s`       | A space, tab or new line                                                       |
| `\S`       | Anything that is not a space                                                   |
| `[abc]`    | One of `a`, `b` or `c`                                                   |
| `[a-z]`    | One lowercase letter                                                           |
| `[A-Za-z]` | One letter                                                                     |
| `[^0-9]`   | One character that is **not** a digit (`^` inside `[ ]` means "not") |

```python
print(re.findall(r"[aeiou]", "regular expression"))
# ['e', 'u', 'a', 'e', 'e', 'i', 'o']          (the vowels)

print(re.findall(r"[^0-9]+", "ab12cd3"))        # ['ab', 'cd']
print(re.findall(r"[A-Z][a-z]+", "Hello World from Python"))     # ['Hello', 'World', 'Python']   (a capital letter, then small letters)
print(re.findall(r"\w+", "Hello, world_1!"))    # ['Hello', 'world_1']
print(re.findall(r"\W", "a-b c"))               # ['-', ' ']
```

### 3. Quantifiers: how many times

| Pattern   | Meaning                |
| --------- | ---------------------- |
| `*`     | 0 or more times        |
| `+`     | 1 or more times        |
| `?`     | 0 or 1 time (optional) |
| `{3}`   | Exactly 3 times        |
| `{2,3}` | 2 to 3 times           |
| `{2,}`  | 2 or more times        |

```python
print(re.findall(r"colou?r", "color colour colr"))     # ['color', 'colour']   (the u is optional)
print(re.findall(r"\d{3}", "12 123 1234"))             # ['123', '123']       (3 digits, 1234 gives 123 only)
print(re.findall(r"\d{2,3}", "1 12 123 1234"))         # ['12', '123', '123']
```

### 4. Anchors: where

| Pattern | Meaning                              |
| ------- | ------------------------------------ |
| `^`   | Start of the text                    |
| `$`   | End of the text                      |
| `\b`  | A word boundary (the edge of a word) |

```python
print(re.findall(r"\bcat\b", "cat concat cat."))    # ['cat', 'cat']   (the whole word cat only, not inside concat)
print(re.findall(r"^\d+", "123 abc 456"))           # ['123']          (digits at the start)
print(re.findall(r"\d+$", "abc 456"))               # ['456']          (digits at the end)
```

### 5. Alternation: this or that

```python
print(re.findall(r"cat|dog", "cat dog bird cat"))     # ['cat', 'dog', 'cat']
```

### 6. Groups `( )`: pick parts of a match

Brackets make a **group**. `group(1)` is the first bracket, `group(2)` the second.

```python
m = re.search(r"(\d{2})-(\d{2})-(\d{4})", "Date: 25-10-2026")

print(m.group())        # 25-10-2026   (the whole match)
print(m.group(1))       # 25
print(m.groups())       # ('25', '10', '2026')
```

**Named groups** `(?P<name>...)` are easier to read:

```python
m = re.search(r"(?P<day>\d{2})-(?P<month>\d{2})-(?P<year>\d{4})", "Date: 25-10-2026")

print(m.groupdict())    # {'day': '25', 'month': '10', 'year': '2026'}
print(m["year"])        # 2026
```

Use a group in `re.sub()` with `\1`, `\2` to rearrange the text:

```python
print(re.sub(r"(\w+) (\w+)", r"\2 \1", "hello world"))     # world hello
```

### 7. Greedy and lazy

A quantifier takes **as much as possible** (greedy). Add `?` after it to take **as little as possible** (lazy).

```python
print(re.search(r"<.+>", "<b>bold</b>").group())      # <b>bold</b>   (greedy: up to the last >)
print(re.search(r"<.+?>", "<b>bold</b>").group())     # <b>           (lazy: up to the first >)
```

### 8. Flags

A flag changes how the pattern works. The common one is `re.IGNORECASE` (or `re.I`).

```python
print(re.findall(r"python", "Python python PYTHON", re.IGNORECASE))     # ['Python', 'python', 'PYTHON']
```

## Worked example: decimal numbers and version numbers

### Explaining `re.search(r"\d+\.\d+", s)`

```python
s = "Python 3.12 is great"
m = re.search(r"\d+\.\d+", s)
```

This looks for a **decimal number**: digits, a dot, then more digits.

| Part | Meaning |
| ---- | ------- |
| `re.search(...)` | Look through the text from left to right and return the **first** match |
| `r"..."` | A raw string, so Python leaves the backslashes for the regex |
| `\d+` | One or more digits |
| `\.` | A **real dot**. The backslash is needed because a plain `.` means "any character" |
| `\d+` | One or more digits again |
| `s` | The text to search in |
| `m` | The result: a match object, or `None` if nothing matched |

How it matches `"Python 3.12 is great"`, from left to right:

1. `Python` and the space: no digit here, so the pattern cannot start.
2. At `3` (position 7): `\d+` matches `3`.
3. Next is `.`: `\.` matches it.
4. Next is `12`: the second `\d+` matches it.
5. Done. The matched text is `3.12`, at positions 7 to 11.

```python
print(m)           # <re.Match object; span=(7, 11), match='3.12'>
print(m.group())   # 3.12
print(m.span())    # (7, 11)
```

Why `\.` and not `.`: a plain `.` accepts any character in the middle.

```python
re.search(r"\d+.\d+", "x 3a12").group()    # 3a12   (wrong: the dot matched the letter a)
re.search(r"\d+\.\d+", "x 3a12")           # None   (correct: there is no real dot)
```

| Text | Result | Why |
| ---- | ------ | --- |
| `"price 45.50 and 3.5"` | `45.50` | `search` returns only the **first** match |
| `"version 12"` | `None` | There is no dot |
| `"3."` | `None` | There are no digits after the dot |
| `".5"` | `None` | There are no digits before the dot |

To get **all** the decimal numbers, use `findall`:

```python
re.findall(r"\d+\.\d+", "price 45.50 and 3.5 and 7")     # ['45.50', '3.5']   (7 has no dot, so it is skipped)
```

### Version numbers like `3.14.2`

The pattern `\d+\.\d+` stops after two parts, so on `3.14.2` it returns only `3.14`. To match a version with any number of dots, **repeat** the "dot + digits" part:

```python
re.search(r"\d+(?:\.\d+)+", "Python 3.14.2 is out").group()     # 3.14.2
```

| Part | Meaning |
| ---- | ------- |
| `\d+` | The first number (`3`) |
| `(?:\.\d+)` | A dot followed by digits (`.14`). The `?:` makes it a group that is not saved |
| `+` after the group | Repeat that group **1 or more times**, so `.14` and then `.2` |

```python
s = "Python 3.14.2 is out, older is 3.12 and 2.7.18.1"

print(re.findall(r"\d+(?:\.\d+)+", s))
# ['3.14.2', '3.12', '2.7.18.1']
```

Other cases:

```python
# Exactly 3 parts (major.minor.patch)
re.search(r"\d+\.\d+\.\d+", s).group()               # 3.14.2
re.fullmatch(r"\d+(?:\.\d+){2}", "3.14.2")           # matches
re.fullmatch(r"\d+(?:\.\d+){2}", "3.14")             # None (only 2 parts)

# The third part is optional (matches both 3.12 and 3.14.2)
re.findall(r"\d+\.\d+(?:\.\d+)?", s)
# ['3.14.2', '3.12', '2.7.18']      (it allows only 3 parts, so the last part of 2.7.18.1 is cut off)

# Get each part with named groups
m = re.search(r"(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)", "Python 3.14.2")
print(m.groupdict())                          # {'major': '3', 'minor': '14', 'patch': '2'}

# Or split the matched text and make numbers
parts = m.group().split(".")                  # ['3', '14', '2']
print([int(x) for x in parts])                # [3, 14, 2]
```

A common mistake: do not use `(\.\d+)+` with normal brackets when you use `findall`. `findall` returns the **group** and not the whole match, and only the last repeat:

```python
re.findall(r"\d+(\.\d+)+", s)      # ['.2', '.12', '.1']   (wrong)
re.findall(r"\d+(?:\.\d+)+", s)    # ['3.14.2', '3.12', '2.7.18.1']   (correct, with ?:)
```

## Ready patterns (for practice)

```python
# Email (a simple pattern, not a full validation)
print(re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", "Mail a.b@x.com or c@y.org now"))
# ['a.b@x.com', 'c@y.org']

# 10-digit mobile number starting with 6, 7, 8 or 9
print(re.findall(r"[6-9]\d{9}", "Call 9876543210 or 1234567890 or 8123456789"))
# ['9876543210', '8123456789']

# 6-digit PIN code (whole number only)
print(re.findall(r"\b\d{6}\b", "PIN 500001 and 12345"))     # ['500001']

# Date like 2026-10-25
print(re.fullmatch(r"\d{4}-\d{2}-\d{2}", "2026-10-25") is not None)     # True
print(re.fullmatch(r"\d{4}-\d{2}-\d{2}", "26-10-25") is not None)       # False
```

How to read the email pattern `[\w.+-]+@[\w-]+\.[\w.]+`:

| Part         | Meaning                                                                           |
| ------------ | --------------------------------------------------------------------------------- |
| `[\w.+-]+` | One or more letters, digits, `_`, `.`, `+` or `-` (the name before `@`) |
| `@`        | The `@` sign                                                                    |
| `[\w-]+`   | One or more letters, digits, `_` or `-` (the domain, like `gmail`)          |
| `\.`       | A real dot                                                                        |
| `[\w.]+`   | One or more letters, digits, `_` or `.` (like `com` or `co.in`)           |

## Regex in Pandas: cleaning `raw_data.xlsx`

Pandas has the same power on a whole column through `.str` methods:

| Pandas method                         | What it does                                     | Like                       |
| ------------------------------------- | ------------------------------------------------ | -------------------------- |
| `s.str.replace(p, new, regex=True)` | Replace the matches in every row                 | `re.sub`                 |
| `s.str.extract(p)`                  | Take the first group of the match from every row | `re.search` with a group |
| `s.str.contains(p)`                 | `True` or `False` for every row              | `re.search`              |
| `s.str.findall(p)`                  | A list of all matches in every row               | `re.findall`             |

- In Pandas, `str.replace()` needs `regex=True` to use a pattern.
- Empty cells (`NaN`) stay `NaN`, so no error.

The file `raw_data.xlsx` has symbols in the text and numbers hidden inside text:

```python
import pandas as pd

df = pd.read_excel("raw_data.xlsx")
print(df)
#      Name          Domain       Age   Location   Salary      Exp
# 0    Mike   Datascience#$  34 years     Mumbai   5^00#0       2+
# 1  Teddy^         Testing    45' yr  Bangalore  10%%000       <3
# 2   Uma#r  Dataanalyst^^#       NaN        NaN  1$5%000   4> yrs
# 3    Jane     Ana^^lytics       NaN   Hyderbad   2000^0      NaN
# 4  Uttam*      Statistics     67-yr        NaN   30000-  5+ year
# 5     Kim             NLP      55yr      Delhi  6000^$0      10+
```

**Find the rows with symbols**

```python
print(df["Domain"].str.contains(r"[^A-Za-z]").tolist())
# [True, False, True, True, False, False]
```

`[^A-Za-z]` is any character that is not a letter. `True` means the row has a symbol.

**Step 1: Name and Domain: remove everything that is not a letter**

```python
clean = df.copy()
for col in ["Name", "Domain"]:
    clean[col] = clean[col].str.replace(r"[^A-Za-z]", "", regex=True)
```

`Teddy^` becomes `Teddy`, `Uma#r` becomes `Umar`, `Datascience#$` becomes `Datascience`.

**Step 2: Salary: remove everything that is not a digit, then make it a number**

```python
clean["Salary"] = clean["Salary"].str.replace(r"\D", "", regex=True).astype(int)
```

`\D` means "not a digit". `5^00#0` becomes `5000`, and `10%%000` becomes `10000`.

**Step 3: Age and Exp: take the number out of the text**

```python
clean["Age"] = pd.to_numeric(clean["Age"].str.extract(r"(\d+)")[0])
clean["Exp"] = pd.to_numeric(clean["Exp"].str.extract(r"(\d+)")[0])
```

`(\d+)` is a group of one or more digits. `str.extract()` returns that group. `34 years` becomes `34`, `45' yr` becomes `45`, `<3` becomes `3`, `5+ year` becomes `5`.

**Result**

```python
print(clean)
#     Name       Domain   Age   Location  Salary   Exp
# 0   Mike  Datascience  34.0     Mumbai    5000   2.0
# 1  Teddy      Testing  45.0  Bangalore   10000   3.0
# 2   Umar  Dataanalyst   NaN        NaN   15000   4.0
# 3   Jane    Analytics   NaN   Hyderbad   20000   NaN
# 4  Uttam   Statistics  67.0        NaN   30000   5.0
# 5    Kim          NLP  55.0      Delhi   60000  10.0

print(clean.dtypes)
# Name, Domain, Location: text | Age, Exp: float64 | Salary: int64
```

- `Age` and `Exp` are `float64` because they still have empty cells (`NaN`). Fill them next with the mean or the median (the missing value step of EDA).
- Regex only fixes the **symbols**. Spelling mistakes like `Hyderbad` (it should be Hyderabad) need a person to decide, or a lookup list.

## Common mistakes

| Mistake                                                   | Fix                                                   |
| --------------------------------------------------------- | ----------------------------------------------------- |
| Writing `"\d+"` without `r`                           | Always use `r"\d+"`                                 |
| Using `re.match()` and expecting a search in the middle | Use `re.search()`                                   |
| Using `.group()` when `re.search()` returned `None` | Check `if m:` first                                 |
| Forgetting to escape `. ? * + ( ) [ ] { } $ ^ \|`        | Put `\` before the character, like `\.` or `\$` |
| Greedy pattern takes too much (`<.+>`)                  | Use the lazy form `<.+?>`                           |
| `str.replace(r"\d", "")` in Pandas does nothing         | Add `regex=True`                                    |

## Quick reference

| Pattern                        | Meaning                        |
| ------------------------------ | ------------------------------ |
| `.`                          | Any character (not a new line) |
| `\d` `\D`                  | Digit / not a digit            |
| `\w` `\W`                  | Letter, digit or `_` / not   |
| `\s` `\S`                  | Space / not a space            |
| `[abc]` `[a-z]` `[^abc]` | One of / a range / not these   |
| `*` `+` `?`              | 0 or more / 1 or more / 0 or 1 |
| `{n}` `{n,m}`              | Exactly n / n to m             |
| `^` `$` `\b`             | Start / end / word boundary    |
| `a\|b`                        | a or b                         |
| `( )` `(?P<name>...)`      | Group / named group            |
| `+?` `*?`                  | Lazy (as little as possible)   |
