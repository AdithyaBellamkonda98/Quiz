import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('climate.db')
cursor = conn.cursor()

# Fetch data from the ClimateData table
cursor.execute('SELECT Year, CO2, Temperature FROM ClimateData')
data = cursor.fetchall()

# Separate the data into lists
years_list = []
co2_list = []
temp_list = []

for row in data:
    years_list.append(row[0])
    co2_list.append(row[1])
    temp_list.append(row[2])

# Close the database connection
conn.close()

# Create the subplots and plot the data
plt.subplot(2, 1, 1)
plt.plot(years_list, co2_list, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years_list, temp_list, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.show() 
plt.savefig("co2_temp_1.png")
