import pandas as pd

# Function to map parsed output to DataFrame
def map_categories_to_dataframe(parsed_output, original_df, transaction_column):
    categories = []
    for idx, transaction in enumerate(original_df[transaction_column].astype(str).tolist()):
        # Find the corresponding category
        if idx < len(parsed_output):
            categories.append(parsed_output[idx]['category'])
        else:
            categories.append(None)  # Handle missing categories
    # Add 'Category' column to DataFrame
    original_df['Category'] = categories
    return original_df