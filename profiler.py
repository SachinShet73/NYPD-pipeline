import pandas as pd
from ydata_profiling import ProfileReport

# Load the data
df = pd.read_csv('data/raw/NYPD_Arrests_Data__Historic_reduced.csv')

# Generate profiling report
profile = ProfileReport(df, 
                       title="NYPD Arrests Data Profile",
                       explorative=True,
                       minimal=False)

# Save report
profile.to_file("data/profiling/nypd_arrests_profile.html")

print(f"Dataset shape: {df.shape}")
print(f"\nColumn names:\n{df.columns.tolist()}")
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nData types:\n{df.dtypes}")