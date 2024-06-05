import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 5))
print("Test Data:")
print(df)

# Save the data to a CSV file
df.to_csv("data.csv", index=False)