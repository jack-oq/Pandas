import pandas as pd

# Assuming you have a DataFrame named 'produce_data'
# with columns 'produce_name' and 'quantity_sold'

# Sample data for demonstration purposes
data = {
    'produce_name': ['Apples', 'Bananas', 'Carrots', 'Oranges', 'Grapes'],
    'quantity_sold': [12000, 10000, 11500, 11800, 13000]
}

produce_data = pd.DataFrame(data)

# Filter the DataFrame based on the condition
produce_new = produce_data[(produce_data['quantity_sold'] >= 11500) & (produce_data['quantity_sold'] <= 12000)]

# Display the new DataFrame
print(produce_new)
