# Importing the folium library
import folium

# Step 1: Creating a map centered on Dhule, Maharashtra, India
maharashtra_map = folium.Map(location=[20.9042, 74.7749], zoom_start=10, tiles='Stamen Terrain')

# Step 2: Adding markers to the map for nearby cities
# Adding a marker at Dhule
folium.Marker([20.9042, 74.7749], popup="Dhule").add_to(maharashtra_map)

# Adding a marker at Malegaon
folium.Marker([20.5500, 74.5333], popup="Malegaon").add_to(maharashtra_map)

# Adding a marker at Jalgaon
folium.Marker([21.0067, 75.5626], popup="Jalgaon").add_to(maharashtra_map)

# Adding a marker at Nasik
folium.Marker([19.9975, 73.7898], popup="Nasik").add_to(maharashtra_map)

# Adding a marker at Aurangabad
folium.Marker([19.8762, 75.3433], popup="Aurangabad").add_to(maharashtra_map)

# Step 3: Choropleth Map for Maharashtra (simplified, using hypothetical population data for districts)
# Sample data for district populations (hypothetical example, usually you would use actual data)
district_population = {
    'Dhule': 2050863, 'Malegaon': 4710065, 'Jalgaon': 4224442, 
    'Nasik': 6109052, 'Aurangabad': 3701282
}

# Choropleth map: Using hypothetical values as a demonstration
# In practice, you would use a GeoJSON file with boundaries for the districts and the actual population data
maharashtra_map.choropleth(
    geo_data='district_boundaries.geojson',  # You would use the actual GeoJSON data for districts
    data=district_population,
    columns=['District', 'Population'],
    key_on='feature.properties.name',  # Assuming the district names in the GeoJSON file
    fill_color='YlGnBu',  # Color scheme
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Population'
)

# Step 4: Display the map with markers and choropleth
maharashtra_map
