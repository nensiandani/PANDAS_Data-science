import pandas as pd
import numpy as np

# IPL players dataset
data = {
    'Player': ['Virat', 'Rohit', 'Dhoni', 'Hardik'],
    'Runs': [540, 460, 400, 370],
    'Matches': [14, 13, 15, 12]
}

df = pd.DataFrame(data)

# Strike Rate (runs per match)
df['StrikeRate'] = df['Runs'] / df['Matches']

# Highest Run Scorer
top_batsman = df.loc[df['Runs'].idxmax(), 'Player']

print("🏏 IPL Player Stats:")
print(df)
print(f"\n🏆 Highest Run Scorer: {top_batsman}")

'''
🏏 IPL Player Stats:
   Player  Runs  Matches  StrikeRate
0   Virat   540       14   38.571429
1   Rohit   460       13   35.384615
2   Dhoni   400       15   26.666667
3  Hardik   370       12   30.833333

🏆 Highest Run Scorer: Virat
'''