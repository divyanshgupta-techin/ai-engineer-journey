# ============================================================
# DAY 03 - PYTHON BASICS REVISION
# AI ENGINEER JOURNEY
# ============================================================
#
# Today's Revision:
# 1. Variables
# 2. Data Types
# 3. Operators
#
# This file is part of my public AI Engineer Journey.
# ============================================================


# ============================================================
# 1. VARIABLES
# ============================================================

print("\n========== VARIABLES ==========\n")

# Basic variable assignment
name = "Divyansh"
age = 18
Marks = 9.9
is_learning_ai = True

print("Name:", name)
print("Age:", age)
print("Marks:", Marks)
print("Learning AI:", is_learning_ai)


# Multiple variables
first_name = "Divyansh"
last_name = "Gupta"

print("\nFirst Name:", first_name)
print("Last Name:", last_name)


# Multiple assignment in one line
python, ai, ml = "Python", "Artificial Intelligence", "Machine Learning"

print("\nSubjects:")
print(python)
print(ai)
print(ml)


# Swapping two variables
a = 10
b = 20

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter swapping:")
print("a =", a)
print("b =", b)


# ============================================================
# 2. DATA TYPES
# ============================================================

print("\n========== DATA TYPES ==========\n")

# Integer
age = 18

# Float
Marks = 9.9

# String
name = "Divyansh"

# Boolean
is_ai_engineer = False

print("age:", age)
print("Marks:", Marks)
print("name:", name)
print("is_ai_engineer:", is_ai_engineer)


# Checking data types using type()
print("\nData Types:")

print(type(age))
print(type(Marks))
print(type(name))
print(type(is_ai_engineer))


# ============================================================
# TYPE CONVERSION
# ============================================================

print("\n========== TYPE CONVERSION ==========\n")

# String to Integer
age_text = "18"
age_number = int(age_text)

print("Original value:", age_text)
print("Converted value:", age_number)
print("Type:", type(age_number))


# Integer to Float
number = 10
decimal_number = float(number)

print("\nInteger:", number)
print("Converted to float:", decimal_number)


# Number to String
score = 95
score_text = str(score)

print("\nScore:", score)
print("Score as string:", score_text)
print("Type:", type(score_text))


# ============================================================
# 3. OPERATORS
# ============================================================

print("\n========== OPERATORS ==========\n")

a = 20
b = 6


# ----------------------------
# Arithmetic Operators
# ----------------------------

print("----- Arithmetic Operators -----")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# ----------------------------
# Comparison Operators
# ----------------------------

print("\n----- Comparison Operators -----")

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# ----------------------------
# Logical Operators
# ----------------------------

print("\n----- Logical Operators -----")

age = 18
has_python_knowledge = True

print("age >= 18:", age >= 18)
print("has_python_knowledge:", has_python_knowledge)

print(
    "Eligible:",
    age >= 18 and has_python_knowledge
)

print(
    "At least one condition:",
    age >= 18 or has_python_knowledge
)

print(
    "Not an adult:",
    not (age >= 18)
)


# ----------------------------
# Assignment Operators
# ----------------------------

print("\n----- Assignment Operators -----")

score = 10

print("Initial score:", score)

score += 5
print("After += 5:", score)

score -= 2
print("After -= 2:", score)

score *= 2
print("After *= 2:", score)

score /= 2
print("After /= 2:", score)


# ============================================================
# PYTHON TIPS I REVISED TODAY
# ============================================================

print("\n========== PYTHON TIPS ==========\n")


# TIP 1: Swap values without a temporary variable

x = 100
y = 200

x, y = y, x

print("TIP 1 - Swapping:")
print("x =", x)
print("y =", y)


# TIP 2: Multiple assignment

name, age = "Divyansh", 18

print("\nTIP 2 - Multiple Assignment:")
print("Name:", name)
print("Age:", age)


# TIP 3: Chained comparisons

age = 18

print("\nTIP 3 - Chained Comparison:")

if 18 <= age <= 25:
    print("Age is between 18 and 25")


# ============================================================
# QUICK REVISION
# ============================================================

print("\n========== QUICK REVISION ==========\n")

print("Variables:")
print("- Used to store values.")
print("- Python does not require explicit variable type declaration.")

print("\nData Types:")
print("- int")
print("- float")
print("- str")
print("- bool")

print("\nOperators:")
print("- Arithmetic")
print("- Comparison")
print("- Logical")
print("- Assignment")


# ============================================================
# DAY 03 COMPLETE
# ============================================================

print("\n========================================")
print("DAY 03 - PYTHON BASICS REVISION DONE!")
print("========================================")

print("\nToday's topics:")
print("✓ Variables")
print("✓ Data Types")
print("✓ Operators")

print("\nNext:")
print("Day 04 - Python Input/Output Practice")
print("15 Questions | 90 Seconds Challenge")

# ============================================================
# END
# ============================================================