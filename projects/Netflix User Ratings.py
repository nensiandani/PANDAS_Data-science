
import pandas as pd
import numpy as np
# Netflix ratings dataset
data = {
    'User': ['U1', 'U2', 'U3', 'U4'],
    'Movie1': [5, 4, np.nan, 5],
    'Movie2': [4, 5, 3, np.nan],
    'Movie3': [np.nan, 2, 4, 3]
}

df = pd.DataFrame(data)

# Fill missing ratings with average rating
df_filled = df.fillna(df.mean())

# Find average rating per movie
avg_ratings = df_filled[['Movie1', 'Movie2', 'Movie3']].mean()

print("🎬 Netflix Ratings:")
print(df_filled)
print("\n⭐ Average Ratings per Movie:")
print(avg_ratings)


'''
🎬 Netflix Ratings:
  User    Movie1    Movie2    Movie3
0   U1  5.000000  4.000000  3.000000
1   U2  4.000000  5.000000  2.000000
2   U3  4.666667  3.000000  4.000000
3   U4  5.000000  4.000000  3.000000

⭐ Average Ratings per Movie:
Movie1    4.666667
Movie2    4.000000
Movie3    3.000000
dtype: float64


'''