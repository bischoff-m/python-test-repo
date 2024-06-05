from pathlib import Path
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 5))
print("Test Data:")
print(df)

# Save the data to a CSV file
root_path = Path(__file__).parent.parent
df.to_csv(root_path / "data.csv", index=False)