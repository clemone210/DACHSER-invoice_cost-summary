import os
import pandas as pd

# List all files in the 'invoices' directory with a .csv extension
invoice_files = [f for f in os.listdir('invoices') if f.endswith('.csv')]

# Check if there are any invoice files
if not invoice_files:
    print("No invoice files found.")
    exit()

all_dataframes = []

for file in invoice_files:
    path = os.path.join('invoices', file)
    df = pd.read_csv(path, delimiter=';')

    # Filter rows where 'Leistungsartenbezeichnung' is not empty
    df = df[df['Leistungsartenbezeichnung'].notna()]

    all_dataframes.append(df)

# Concatenate all the dataframes
final_df = pd.concat(all_dataframes, ignore_index=True)

# Create the detailed overview DataFrame
output_df = final_df[['Erstauftragsnummer', 'Leistungsartenbezeichnung', 'Leistungsarten-Nettobetrag']]

# Ensure the 'Leistungsarten-Nettobetrag' column is numeric

# Convert using comma as a decimal separator (European format), for instance
final_df['Leistungsarten-Nettobetrag'] = pd.to_numeric(final_df['Leistungsarten-Nettobetrag'].str.replace(',', '.'), errors='coerce')

# Check if there are any NaN values after conversion
if final_df['Leistungsarten-Nettobetrag'].isna().any():
    print("Warning: Some values in 'Leistungsarten-Nettobetrag' could not be converted to numeric format. They have been set to NaN.")

# Sum the cost for each "Erstauftragsnummer"
summary_df = final_df.groupby('Erstauftragsnummer').agg({'Leistungsarten-Nettobetrag': 'sum'}).reset_index()

# Save both DataFrames to separate sheets in a single Excel file
with pd.ExcelWriter('Invoice-overview.xlsx') as writer:
    output_df.to_excel(writer, sheet_name='Detailed Overview', index=False)
    summary_df.to_excel(writer, sheet_name='Cost Summary', index=False)
