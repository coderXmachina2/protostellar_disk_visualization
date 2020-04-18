#does a bunch of pandas

import pandas as pd
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u

def cat_mag_diam(data, disk_str):
	sorted_disks = data.sort_values(by = disk_str)

	magnitudes = []
	missing_mag = 0

	cat_magnitude_diameter = pd.DataFrame(columns=['Object', 
	                                                'R_band_mag',
	                                                disk_str])

	for index, row in sorted_disks .iterrows():
	    r_band_mag_str = row['R_band_mag']
	    if (isinstance(r_band_mag_str, float)): #the nan got treated as a float
	        missing_mag+=1
	    else:
	        if(r_band_mag_str != '-'):
	            cat_magnitude_diameter = cat_magnitude_diameter.append({'Object': str(row['Object']), 
	                                                    'R_band_mag': float(r_band_mag_str), 
	                                                    disk_str: float(row[disk_str])},
	                                                    ignore_index=True)
	        else:
	             missing_mag+=1

	return(cat_magnitude_diameter)

def plot_astrometry(astrometry):

	return()