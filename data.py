import pandas as pd

files = ["indego-trips-2022-q1.csv", "indego-trips-2022-q2.csv", "indego-trips-2022-q3.csv", "indego-trips-2022-q4.csv",
         "indego-trips-2023-q1.csv", "indego-trips-2023-q2.csv", "indego-trips-2023-q3-2.csv","indego-trips-2023-q4.csv", 
         "indego-trips-2024-q1.csv", "indego-trips-2024-q2.csv", "indego-trips-2024-q3.csv", "indego-trips-2024-q4.csv",
         "indego-trips-2025-q1.csv", "indego-trips-2025-q2.csv", "indego-trips-2025-q3.csv"]

combined_df = pd.concat(
    [pd.read_csv(f) for f in files],
    ignore_index = True,
    sort = False
)

combined_df.dropna(how = 'all', inplace = True)
combined_df.to_csv("combine_indego_trips.csv", index = False)

df = pd.read_csv("combine_indego_trips.csv")
df["start_time"]