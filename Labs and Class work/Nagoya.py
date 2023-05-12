import pandas as pd
import geopandas as gpd

url='https://raw.githubusercontent.com/DSSD-Madison/Nagoya/main/data/GeoDS4Bolivia.geojson'
df=gpd.read_file(url)

print(df.corr())