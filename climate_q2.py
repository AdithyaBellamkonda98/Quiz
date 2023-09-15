import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
df = pd.read_csv('climate.csv')

# Display the data
print(df)

# Extract data into separate lists
years_list = df['Year']
co2_list = df['CO2']
temp_list = df['Temperature']

# Create the subplots and plot the data
plt.subplot(2, 1, 1)
plt.plot(years_list, co2_list, 'b--') 
plt.title("Climate Data from CSV") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years_list, temp_list, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.show() 
