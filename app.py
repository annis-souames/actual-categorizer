import streamlit as st
import pandas as pd
from actual import Actual
from actual.queries import get_transactions, get_categories
from llm import OllamaEngine, PromptGenerator
from config import Config
from utils import map_categories_to_dataframe
import io

# Load configuration
cfg = Config(env_path=".env")

actual_params = {
    "base_url": cfg.get("ACTUAL_SERVER"),
    "password": cfg.get("ACTUAL_PASSWORD"),
    "encryption_password": "",
    "file": cfg.get("ACTUAL_BUDGET_FILE"),
    "data_dir": "./data",
}

st.title("Transaction Categorization App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    # Read CSV using pandas
    df = pd.read_csv(uploaded_file)
    columns = df.columns.tolist()

    # Select column for transaction text
    text_column = st.selectbox("Select the column for transaction text", options=columns)

    # Select column for date (optional)
    date_column = st.selectbox("Select the column for transaction date (optional)", options=['None'] + columns)

    if date_column != 'None':
        # Convert selected date column to datetime
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
        df = df.dropna(subset=[date_column])  # Remove rows with invalid dates

        # Date filters are optional
        enable_date_filter = st.checkbox("Enable date filtering")

        if enable_date_filter:
            min_date = df[date_column].min().date()
            max_date = df[date_column].max().date()

            start_date = st.date_input("Start date", value=min_date, min_value=min_date, max_value=max_date)
            end_date = st.date_input("End date", value=max_date, min_value=min_date, max_value=max_date)

            # Filter transactions by date
            filtered_df = df[(df[date_column] >= pd.to_datetime(start_date)) & (df[date_column] <= pd.to_datetime(end_date))]
        else:
            filtered_df = df
    else:
        st.info("Date column not selected. Date filtering is disabled.")
        filtered_df = df

    # Extract transactions from selected column
    transacts = filtered_df[text_column].astype(str).tolist()

    st.subheader("Transactions:")
    st.write(transacts)

    # Fetch categories from Actual
    cats = []
    with Actual(**actual_params) as actual:
        cats = [c.name for c in get_categories(actual.session)]

    # Select categories with checkboxes
    selected_cats = st.multiselect("Select categories", options=cats, default=cats)

    # Process transactions when button is clicked
    if st.button("Categorize Transactions"):
        if not selected_cats:
            st.error("Please select at least one category.")
        elif not transacts:
            st.error("No transactions to process.")
        else:
            # Generate prompt and invoke LLM
            prompt_gen = PromptGenerator(transactions=transacts, categories=selected_cats)
            prompt = prompt_gen.generate_prompt()

            engine = OllamaEngine(base_url=cfg.get("OLLAMA_SERVER"), model=cfg.get("OLLAMA_MODEL"))
            resp = engine.invoke(prompt)

            parsed = engine.parse_response(resp)

            # Map categories to DataFrame
            result_df = map_categories_to_dataframe(parsed, filtered_df.copy(), text_column)

            st.subheader("Categorized Transactions:")
            st.dataframe(result_df)

            # Add a button to download the DataFrame as CSV
            csv_buffer = io.StringIO()
            result_df.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()

            st.download_button(
                label="Download Categorized Transactions as CSV",
                data=csv_data,
                file_name='categorized_transactions.csv',
                mime='text/csv'
            )
else:
    st.info("Please upload a CSV file to proceed.")
