import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset from CSV
df = pd.read_csv('/home/bharat/bharath/LBP/updated_dataset.csv')

# Shuffle the dataset randomly
df_shuffled = df.sample(frac=1, random_state=42)  # Shuffle with random_state for reproducibility

# Split the shuffled dataset into train, validation, and test sets (80%, 10%, 10%)
train_df, test_val_df = train_test_split(df_shuffled, test_size=0.2, random_state=42)
val_df, test_df = train_test_split(test_val_df, test_size=0.5, random_state=42)

# Write the split datasets to new CSV files if needed
train_df.to_csv('train.csv', index=False)
val_df.to_csv('validation.csv', index=False)
test_df.to_csv('test.csv', index=False)

# Print the sizes of the resulting datasets
print("Train set size:", len(train_df))
print("Validation set size:", len(val_df))
print("Test set size:", len(test_df))
