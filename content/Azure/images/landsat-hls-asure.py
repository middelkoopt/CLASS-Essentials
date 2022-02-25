#!/usr/bin/env python3
# need to install - pip install azure-storage-blob
# https://nbviewer.org/github/microsoft/AIforEarthDataSets/blob/main/data/hls.ipynb

# Environment setup
import requests
import numpy as np
import io
import matplotlib.pyplot as plt
import pandas as pd

import rasterio
from azure.storage.blob import ContainerClient

container_name = 'hls'
storage_account_name = 'hlssa'
storage_account_url = 'https://' + storage_account_name + '.blob.core.windows.net/'
hls_blob_root = storage_account_url + container_name

# This file is provided by NASA; it indicates the lat/lon extents of each
# hls tile.
#
# The file originally comes from:
#
# https://hls.gsfc.nasa.gov/wp-content/uploads/2016/10/S2_TilingSystem2-1.txt
#
# ...but as of 8/2019, there is a bug with the column names in the original file, so we
# access a copy with corrected column names.
hls_tile_extents_url = 'https://ai4edatasetspublicassets.blob.core.windows.net/assets/S2_TilingSystem2-1.txt'

# Load this file into a table, where each row is:
#
# Tile ID, Xstart, Ystart, UZ, EPSG, MinLon, MaxLon, MinLon, MaxLon
s = requests.get(hls_tile_extents_url).content
hls_tile_extents = pd.read_csv(io.StringIO(s.decode('utf-8')),delimiter=r'\s+')
print('Read tile extents for {} tiles'.format(len(hls_tile_extents)))

hls_container_client = ContainerClient(account_url=storage_account_url, 
                                         container_name=container_name,
                                         credential=None)

# Functions

def list_available_tiles(prefix):
    """
    List all blobs in an Azure blob container matching a prefix.  
    
    We'll use this to query tiles by location and year.
    """
    
    files = []
    generator = hls_container_client.list_blobs(name_starts_with=prefix)
    for blob in generator:
        files.append(blob.name)
    return files


def lat_lon_to_hls_tile_id(lat,lon):
    """
    Get the hls tile ID for a given lat/lon coordinate pair.
    """  
    
    found_matching_tile = False

    for i_row,row in hls_tile_extents.iterrows():
        found_matching_tile = lat >= row.MinLat and lat <= row.MaxLat \
        and lon >= row.MinLon and lon <= row.MaxLon
        if found_matching_tile:
            break
    
    if not found_matching_tile:
        return None
    else:
        return row.TilID

# Build a tile path from components, including lat/lon lookup
# Near Bear Lake, UT
# lat = 41.89655047211277; lon = -111.4132464403312 
lat = 39.768402; lon = -86.158066 

tile_id = lat_lon_to_hls_tile_id(lat,lon)
print('Using Tile ID {}'.format(tile_id))

year    = '2019'
daynum  = '001'   # 1-indexed day-of-year
product = 'S30'   # 'S30' for Sentinel, 'L30' for Landsat
sband   = '_01'
version = 'v1.4'  # Currently always v1.4

blob_name = product + '/HLS.' + product + '.T' + tile_id + '.' + year + daynum + '.' + version \
    + sband + '.tif'
sentinel_url = hls_blob_root + '/' + blob_name
print('Constructed tile URL:\n{}'.format(sentinel_url))

# Display an RGB composite of the Sentinel-2 image we just chose
# Bands 2, 3, and 4 are B, G, and R in Sentinel-2 HLS images
composite_bands = [4,3,2]

urls = [sentinel_url.replace(sband,'_' + str(b).zfill(2)) for b in composite_bands]
print('Rendering URLs:')
for s in urls:
    print(s)

image_data = []

composite_downsample_factor = 5
composite_norm_value = 15000

for fn in urls:
    with rasterio.open(fn,'r') as raster:
        h = int(raster.height/composite_downsample_factor)
        w = int(raster.width/composite_downsample_factor)
        band_array = raster.read(1, out_shape=(1, h, w))
        raster.close()
        band_array = band_array / composite_norm_value
        image_data.append(band_array)

rgb = np.dstack((image_data[0],image_data[1],image_data[2]))
np.clip(rgb,0,1,rgb)

dpi = 100; fig = plt.figure(frameon=False,figsize=(w/dpi,h/dpi),dpi=dpi)
ax = plt.Axes(fig,[0., 0., 1., 1.]); ax.set_axis_off(); fig.add_axes(ax)
plt.imshow(rgb);
plt.imsave('test.png', rgb)

i_daynum = int(daynum)
product = 'L30'

# Try days sequentially until we find one where there's a Landsat image for this day
while True:
    
    daynum = str(i_daynum).zfill(3)
    prefix = product + '/HLS.' + product + '.T' + tile_id + '.' + year + daynum
    print('Finding tiles with prefix {}'.format(prefix))
    matches = list_available_tiles(prefix)
    
    if len(matches) == 0:
        print('No matching tiles')
        i_daynum += 1
    else:
        break

blob_name = matches[0]
landsat_url = hls_blob_root + '/' + blob_name
print('Found {} matching tiles, e.g.:\n{}'.format(len(matches),landsat_url))

# Display a composite of the Landsat image we found
urls = [landsat_url.replace(sband,'_' + str(b).zfill(2)) for b in composite_bands]
print('Rendering URLs:')
for s in urls:
    print(s)

image_data = []
for fn in urls:
    with rasterio.open(fn,'r') as raster:
        h = int(raster.height/composite_downsample_factor)
        w = int(raster.width/composite_downsample_factor)
        band_array = raster.read(1, out_shape=(1, h, w))
        raster.close()
        band_array = band_array / composite_norm_value
        image_data.append(band_array)

rgb = np.dstack((image_data[0],image_data[1],image_data[2]))
np.clip(rgb,0,1,rgb)

dpi = 100; fig = plt.figure(frameon=False,figsize=(w/dpi,h/dpi),dpi=dpi)
ax = plt.Axes(fig,[0., 0., 1., 1.]); ax.set_axis_off(); fig.add_axes(ax)
plt.imshow(rgb);
plt.show()
