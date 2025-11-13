import pandas as pd

# 1. Load data
df = pd.read_csv('bookings.csv')

# 2. Filter rows where Mode == 'By Air'
df = df[df['Mode'] == 'By Air']

# 3. Calculate total for each row
df['TotalBooking'] = df['ChargedWeight'] * df['RatePerKg'] + df['Collection'] + df['Delivery'] + 100

# 4. Save result
df.to_csv('bookings_with_total.csv', index=False)

print("Done. File saved as bookings_with_total.csv")
