import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
data = pd.read_csv("pune.csv")

# Load Chennai dataset
chennai_data = pd.read_csv("chennai.csv")  # Replace with the correct file path for Chennai dataset


# Convert 'date_time' to datetime format
data['date_time'] = pd.to_datetime(data['date_time'])

# Clean the 'date' column to extract the date and time
chennai_data['date'] = chennai_data['date'].str.extract(r'(\d{1,2} \w+ \d{4})')  # Extract '14 July 2024'
chennai_data['date'] = pd.to_datetime(chennai_data['date'], format='%d %B %Y', errors='coerce')  # Convert to datetime

# Drop rows with invalid dates (if any)
chennai_data = chennai_data.dropna(subset=['date'])

# Print column names for verification
print("Column Names in Dataset:", data.columns)

# Calculate temperature statistics
average_temp = data['tempC'].mean()
max_temp = data['tempC'].max()
min_temp = data['tempC'].min()

# Calculate rainfall statistics
average_rainfall = data['precipMM'].mean()
max_rainfall = data['precipMM'].max()
min_rainfall = data['precipMM'].min()

# Calculate humidity statistics
average_humidity = data['humidity'].mean()
max_humidity = data['humidity'].max()
min_humidity = data['humidity'].min()

# Print statistics
print(f"Temperature - Average: {average_temp:.2f}°C, Max: {max_temp}°C, Min: {min_temp}°C")
print(f"Rainfall - Average: {average_rainfall:.2f} mm, Max: {max_rainfall} mm, Min: {min_rainfall} mm")
print(f"Humidity - Average: {average_humidity:.2f}%, Max: {max_humidity}%, Min: {min_humidity}%")

# Detect extreme weather events
heatwave_threshold = 40  # Example threshold for heatwave
heavy_rainfall_threshold = 10  # Example threshold for heavy rainfall

extreme_heat_days = data[data['tempC'] > heatwave_threshold]
heavy_rainfall_days = data[data['precipMM'] > heavy_rainfall_threshold]

# Print extreme weather event details
print("\nExtreme Heat Events:")
print(extreme_heat_days[['date_time', 'tempC']])
print("\nHeavy Rainfall Events:")
print(heavy_rainfall_days[['date_time', 'precipMM']])

# Plot temperature trends over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='date_time', y='tempC', label='Temperature (°C)', color='orange')
plt.axhline(y=heatwave_threshold, color='red', linestyle='--', label='Heatwave Threshold')
plt.title('Temperature Trends Over Time in Pune')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot humidity trends over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='date_time', y='humidity', label='Humidity (%)', color='green')
plt.title('Humidity Trends Over Time in Pune')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot temperature vs humidity
plt.figure(figsize=(12, 6))
sns.scatterplot(data=data, x='tempC', y='humidity', color='blue')
plt.title('Temperature vs Humidity in Pune')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.tight_layout()
plt.show()

# Plot temperature trends for Chennai
plt.figure(figsize=(12, 6))
sns.lineplot(data=chennai_data, x='date', y='temp', label='Chennai Temperature (°C)', color='blue')
plt.title('Temperature Trends Over Time in Chennai')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Plot humidity trends for Chennai
plt.figure(figsize=(12, 6))
sns.lineplot(data=chennai_data, x='date', y='hum', label='Chennai Humidity (%)', color='green')
plt.title('Humidity Trends Over Time in Chennai')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# Combined Temperature Trend for Pune and Chennai
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='date_time', y='tempC', label='Pune Temperature (°C)', color='orange')
sns.lineplot(data=chennai_data, x='date', y='temp', label='Chennai Temperature (°C)', color='blue')
plt.title('Temperature Trends: Pune vs Chennai')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Combined Humidity Trend for Pune and Chennai
plt.figure(figsize=(12, 6))
sns.lineplot(data=data, x='date_time', y='humidity', label='Pune Humidity (%)', color='green')
sns.lineplot(data=chennai_data, x='date', y='hum', label='Chennai Humidity (%)', color='purple')
plt.title('Humidity Trends: Pune vs Chennai')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


# Interactive temperature trend
fig = px.line(data, x='date_time', y='tempC', title='Interactive Temperature Trend in Pune',
              labels={'date_time': 'Date', 'tempC': 'Temperature (°C)'})
fig.update_layout(xaxis_title='Date', yaxis_title='Temperature (°C)', xaxis=dict(tickangle=45))
fig.show()

# Highlight extreme events on a timeline (optional)
fig = px.scatter(data, x='date_time', y='tempC', title='Extreme Weather Events Over Time',
                 labels={'date_time': 'Date', 'tempC': 'Temperature (°C)'},
                 color_discrete_sequence=['orange'])
fig.add_scatter(x=extreme_heat_days['date_time'], y=extreme_heat_days['tempC'], mode='markers', name='Heatwave Days', marker=dict(color='red'))
fig.add_scatter(x=heavy_rainfall_days['date_time'], y=heavy_rainfall_days['precipMM'], mode='markers', name='Heavy Rainfall Days', marker=dict(color='blue'))
fig.show()






