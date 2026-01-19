# Weather-Data-Analysis-Pune-vs-Chennai

## Overview
This project analyzes and visualizes weather trends for Pune and Chennai using historical temperature and humidity data. The aim is to identify patterns, extreme weather events, and key differences between the two cities' climates.

## Key Steps Taken
1. **Data Collection**  
   - Imported weather datasets for Pune and Chennai.

2. **Data Cleaning**  
   - Converted date fields to proper datetime formats.  
   - Handled missing or invalid entries via dropping or imputation.

3. **Data Analysis**  
   - Calculated statistical measures (mean, max, min) for temperature and humidity.  
   - Identified extreme weather events such as heatwaves and heavy rainfall.

4. **Visualization**  
   - Created line plots to visualize temperature and humidity trends.  
   - Overlaid trends for comparison on combined graphs.  
   - Optional: Interactive graphs using Plotly.

5. **Finalization**  
   - Highlighted key insights in the results section and prepared summary conclusions.

## Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Plotly (optional)

## Code Snippets

### Data Loading and Cleaning
```python
import pandas as pd

# Load datasets
pune_data = pd.read_csv("pune.csv")
chennai_data = pd.read_csv("chennai.csv")

# Convert date columns
pune_data['date_time'] = pd.to_datetime(pune_data['date_time'])
chennai_data['date'] = pd.to_datetime(chennai_data['date'], format='%d %B %Y', errors='coerce')
