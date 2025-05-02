import pandas as pd
import numpy as np

# Create a DataFrame (normally you would load from CSV)
data = {
    'Student': ['A', 'B', 'C', 'D', 'E'],
    'Math': [85, 76, 90, 65, 88],
    'Science': [78, 85, 88, 70, 95],
    'English': [92, 83, 75, 72, 90],
    'History': [88, 80, 95, 60, 92]
}

df = pd.DataFrame(data)

print("📋 Original Dataset:")
print(df)

# -------------------
# Analysis starts here
# -------------------

# 1. Total Marks
df['Total'] = df[['Math', 'Science', 'English', 'History']].sum(axis=1)

# 2. Average Marks
df['Average'] = df['Total'] / 4

# 3. Grade Calculation
def get_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80:
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'

df['Grade'] = df['Average'].apply(get_grade)

# 4. Highest Scorer
topper = df.loc[df['Total'].idxmax(), 'Student']

# 5. Lowest Scorer
lowest = df.loc[df['Total'].idxmin(), 'Student']

# 6. Standard Deviation Subject-Wise
std_subjects = df[['Math', 'Science', 'English', 'History']].std()

# 7. Mean using NumPy
mean_marks = np.mean(df[['Math', 'Science', 'English', 'History']].values)

# -------------------
# Results
# -------------------

print("\n🎯 Student Performance:")
print(df[['Student', 'Total', 'Average', 'Grade']])

print(f"\n🏆 Topper: {topper}")
print(f"😥 Lowest Scorer: {lowest}")

print("\n📊 Subject-wise Standard Deviation:")
print(std_subjects)

print(f"\n🔢 Overall Mean Marks (using NumPy): {mean_marks:.2f}")



'''
📋 Original Dataset:
  Student  Math  Science  English  History
0       A    85       78       92       88
1       B    76       85       83       80
2       C    90       88       75       95
3       D    65       70       72       60
4       E    88       95       90       92

🎯 Student Performance:
  Student  Total  Average Grade
0       A    343    85.75     A
1       B    324    81.00     A
2       C    348    87.00     A
3       D    267    66.75     C
4       E    365    91.25    A+

🏆 Topper: E
😥 Lowest Scorer: D

📊 Subject-wise Standard Deviation:
Math       10.329569
Science     9.576012
English     8.848729
History    14.035669
dtype: float64

🔢 Overall Mean Marks (using NumPy): 82.35
'''