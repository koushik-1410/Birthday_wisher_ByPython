import pandas as pd

# Step 1: Load the original Google Form response CSV
df = pd.read_csv("gform.csv")   # change filename as needed

# Step 2: Select only required columns
filtered_df = df[[
    "Enter Your First name(No space at the end)",
    "Enter your date of Birth",
    "Enter your Phone No(10 digit no only)"
]]

# Step 3: Rename columns (optional, to make it clean)
filtered_df.columns = ["Names", "Birthday", "Phone"]

# Step 4: Save into new CSV
filtered_df.to_csv("birthday_dataset_gform.csv", index=False)

print("Filtered CSV created successfully!")
