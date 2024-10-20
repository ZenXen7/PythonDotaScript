# Import necessary libraries
import pandas as pd
import folium
from folium.plugins import HeatMap

# Load the CSV file with pandas
file_path = 'phivolcs_earthquake_data.csv'
earthquake_data = pd.read_csv(file_path)

# Convert Latitude and Longitude columns to numeric, forcing errors to NaN
earthquake_data['Latitude'] = pd.to_numeric(earthquake_data['Latitude'], errors='coerce')
earthquake_data['Longitude'] = pd.to_numeric(earthquake_data['Longitude'], errors='coerce')

# Drop rows with NaN values in Latitude and Longitude
locations = earthquake_data[['Latitude', 'Longitude']].dropna()

# Create a base map centered around the Philippines (average lat/lon values for visualization)
map_center = [12.8797, 121.7740]  # Center of the Philippines
ph_map = folium.Map(location=map_center, zoom_start=6)

# Add a heatmap to the map using the earthquake locations
heat_data = [[row['Latitude'], row['Longitude']] for index, row in locations.iterrows()]
HeatMap(heat_data).add_to(ph_map)

# Save the map to an HTML file to visualize
map_output_path = 'earthquake_heatmap_philippines.html'  # Save the output file
ph_map.save(map_output_path)

print(f"Heatmap saved to {map_output_path}")
