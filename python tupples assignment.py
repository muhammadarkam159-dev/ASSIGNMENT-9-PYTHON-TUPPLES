# TUPPLE INDEXING
colors = ("red", "green", "blue", "yellow", "purple")
print(colors[1])
print(colors[-1])
print(colors[1:4])

# TUPLE INDEXING
employee = ("Ali", 28, "Data Engineer", 150000)
name, age, job, salary = employee
print(name)
print(salary) 

# TUPLE CONCENTRATION
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
combined = tuple1 + tuple2
print("Combined Tuple:", combined)
reversed_tuple = combined[::-1]
print("Reversed Tuple:", reversed_tuple)

# COUNT AND LOCATE
numbers = (10, 20, 30, 20, 40, 20, 50)
count_20 = numbers.count(20)
first_index = numbers.index(20)
print("Count of 20:", count_20)
print("First index of 20:", first_index)

# EXTENDED TUPLE UNPACKING
data = (100, 200, 300, 400, 500, 600)
first, second, *middle, last = data
middle_list = list(middle)
print("First:", first)
print("Second:", second)
print("Middle List:", middle_list)
print("Last:", last)

# MODIFY AN IMMUTABLE TABLE
numbers = (10, 20, 30, 40, 50)
new_numbers = numbers[:2] + (300,) + numbers[3:]
print("Original Tuple:", numbers)
print("New Tuple:", new_numbers)

# NESTED TUPLE ACCESS
students = (
    ("Ali", (85, 90, 88)),
    ("Sara", (92, 87, 95)),
    ("Ahmed", (78, 84, 80))
)
sara_second_score = students[1][1][1]
ali_scores = students[0][1]
ali_average = sum(ali_scores) / len(ali_scores)
ahmed_scores = students[2][1]
ahmed_highest = max(ahmed_scores)
print("Sara's Second Score:", sara_second_score)
print("Ali's Average Score:", ali_average)
print("Ahmed's Highest Score:", ahmed_highest)

# TUPLE SORTING
employees = (
    ("Ali", 80000),
    ("Sara", 120000),
    ("Ahmed", 95000)
)

salary_sorted = tuple(sorted(employees, reverse=True, key=tuple.__getitem__.__get__(1)))
print(salary_sorted)

# TUPLE MATRIX
matrix = (
    (2, 4, 6),
    (8, 10, 12),
    (14, 16, 18)
)

diagonal = (
    matrix[0][0],
    matrix[1][1],
    matrix[2][2]
)
diagonal_product = (
    diagonal[0] * diagonal[1] * diagonal[2]
)
row_sums = (
    sum(matrix[0]),
    sum(matrix[1]),
    sum(matrix[2])
)
print("Diagonal:", diagonal)
print("Diagonal Product:", diagonal_product)
print("Row Sums:", row_sums)

# INVENTORY TUPLE CHALLENGE
records = (
    ("Laptop", 120000, 5),
    ("Mouse", 1500, 20),
    ("Keyboard", 3500, 10)
)

a, b, c = records

most_expensive = max(
    (a, b, c),
    key=tuple.__getitem__.__get__(1)
)


