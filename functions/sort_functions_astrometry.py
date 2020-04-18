#does a bunch of pandas

import pandas as pd
import numpy as np
from astropy.coordinates import SkyCoord
from astropy import units as u

def astrometry_table(data):
   #

	missing_dist = 0
	astrometry = pd.DataFrame(columns=['Object', 
	                                   'Distance_pc', 
	                                   'Distance_kpc',
	                                   'Distance_ly', 
	                                   'RA_J2000', 
	                                   'DEC_J2000', 
	                                   'RA_J2000_Deci', 
	                                   'DEC_J2000_Deci',
	                                   'Galactic longitude', 
	                                   'Galactic latitude']) #empty pandas array

	for index, row in data.iterrows():
	    dist_pc_str = row['Distance_pc']
	    if (isinstance(dist_pc_str, float)): #the nan got treated as a float
	        #print(str(row['Object']) + ": " + str(dist_pc_str) + " parsecs")
	        
	        #degree minute seconds -> degree decimal
	        #print("Right Ascension: " + str(row['RA_J2000']) + " In degree minute seconds")
	        #print("Declination: " + str(row['DEC_J2000']) + " In degree minute seconds")
	        #print("-")
	        
	        #practice mirror
	        #print(str(row['RA_J2000'][0:2]) + str(row['RA_J2000'][3:5]) + str(row['RA_J2000'][6:11]))#be careful here
	        #print(str(row['DEC_J2000'][1:3]) + str(row['DEC_J2000'][4:6]) + str(row['DEC_J2000'][7:12]))#be careful here
	        
	        RA_Deci = float(row['RA_J2000'][0:2]) + float(row['RA_J2000'][3:5])/60 + float(row['RA_J2000'][6:11])/3600
	        Dec_Deci = float(row['DEC_J2000'][1:3]) + float(row['DEC_J2000'][4:6])/60 + float(row['DEC_J2000'][7:12])/3600
	        
	        if(row['DEC_J2000'][0] == '-'):
	            Dec_Deci *= -1
	        
	        #print("Right Ascension: " + str(RA_Deci) + " In degree decimal")
	        #print("Declination: " + str(Dec_Deci) + " In degree decimal")
	        
	        #convert to galactic coordinates
	        #declination has a sign
	        
	        c_icrs = SkyCoord(ra=RA_Deci*u.degree, dec=Dec_Deci*u.degree, frame='icrs')
	        #print("\nGalactic Coordinates:")
	        #print(c_icrs.galactic.l)
	        #print(c_icrs.galactic.b)

	        #print("\n")
	        astrometry = astrometry.append({'Object': str(row['Object']),
	                                        'Distance_pc': float(dist_pc_str), 
	                                        'Distance_kpc': (float(dist_pc_str)*u.parsec).to(u.kpc),
	                                        'Distance_ly': (float(dist_pc_str)*u.parsec).to(u.lightyear), 
	                                        'RA_J2000': str(row['RA_J2000']),
	                                        'DEC_J2000': str(row['DEC_J2000']), 
	                                        'RA_J2000_Deci': float(RA_Deci), 
	                                        'DEC_J2000_Deci': float(Dec_Deci),
	                                        'Galactic longitude': c_icrs.galactic.l, 
	                                        'Galactic latitude': c_icrs.galactic.b}, ignore_index=True)
	    else:
	        missing_dist+=1

	return(astrometry)

def plot_astrometry(astrometry):
	#load sky coordinates
	c = SkyCoord(astrometry['Galactic longitude'], astrometry['Galactic latitude'], frame='galactic')

	l_rad = c.l.radian
	l_rad[l_rad > np.pi] -= 2. * np.pi
	b_rad = c.b.radian

	return(c, l_rad, b_rad)

def cat_mag_diam(data):
	sorted_objects = data.sort_values(by ='Disk_Major_Axis')

	magnitudes = []
	missing_mag = 0

	cat_magnitude_diameter = pd.DataFrame(columns=['Object', 
	                                                'R_band_mag',
	                                                'Disk_Major_Axis'])

	for index, row in sorted_objects.iterrows():
	    r_band_mag_str = row['R_band_mag']
	    if (isinstance(r_band_mag_str, float)): #the nan got treated as a float
	        missing_mag+=1
	    else:
	        if(r_band_mag_str != '-'):
	            cat_magnitude_diameter = cat_magnitude_diameter.append({'Object': str(row['Object']), 
	                                                    'R_band_mag': float(r_band_mag_str), 
	                                                    'Disk_Major_Axis': float(row['Disk_Major_Axis'])},
	                                                    ignore_index=True)
	        else:
	             missing_mag+=1

	return(cat_magnitude_diameter)