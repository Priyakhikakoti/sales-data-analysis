import pandas as pd


df = pd.read_csv('sales_data.csv')


print("First 5 rows:")
print(df.head())


print("\nDataset Info:")
print(df.info())


print("\nMissing values:")
print(df.isnull().sum())


df.fillna(0, inplace=True)


total_sales = df['Total_Sales'].sum()
average_sales = df['Total_Sales'].mean()
max_sales = df['Total_Sales'].max()


best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()


print("\n--- Sales Analysis Report ---")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Average Sales: ₹{average_sales:,.2f}")
print(f"Highest Sale: ₹{max_sales:,.2f}")
print(f"Best Selling Product: {best_product}")
