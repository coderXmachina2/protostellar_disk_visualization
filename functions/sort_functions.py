#does a bunch of pandas

import pandas as pd
import numpy as np

def sort_mag_spec_type(data):
    #Visualize by spectral class of the catalog!
  missing_spectral_class = 0
  temp_sense = 2

  spectral_bins = [0] * 7  #return this
  spectral_bins_temp = [0] * 21 #return this
  magnitude_spec_type = pd.DataFrame(columns=['Object', 
                                              'Category',
                                              'Spec_Type',
                                              'Magnitude',]) #empty pandas array #retrun this

  for index, row in data.iterrows():
      spec_type_str = row['Spec_Type'] #this is a long string
      r_band_mag_str = row['R_band_mag']
      if (isinstance(spec_type_str, float)):
          print(str(row['Object']) + ": " + str(spec_type_str) + " " + "Spectral Class Data missing")
          print("Magnitude: " + str(r_band_mag_str))
          missing_spectral_class += 1
      else:
          #TODO: Make this smarter.
          if(spec_type_str[0] == 'O'):
              print(str(row['Object']) + ": " + spec_type_str[0:temp_sense] + ' Type Blue Super Massive Star') #Can you print the OBject as well
              spectral_bins[0] += 1
              if(spec_type_str[1] == '0' or spec_type_str[1] == '1' or spec_type_str[1] == '2' or spec_type_str[1] == '3'):
                  spectral_bins_temp[0] += 1  

              elif(spec_type_str[1] == '4' or spec_type_str[1] == '5' or spec_type_str[1] == '6'):
                  spectral_bins_temp[1] += 1

              elif(spec_type_str[1] == '7' or spec_type_str[1] == '8' or spec_type_str[1] == '9'):
                  spectral_bins_temp[2] += 1

              if(isinstance(r_band_mag_str, str)):
                  print("Magnitude: " + str(r_band_mag_str))
                  magnitude_spec_type = magnitude_spec_type.append({'Object': str(row['Object']), 
                                                                    'Category': str(row['Category']),
                                                                    'Spec_Type':str(spec_type_str[0:2]),
                                                                    'Magnitude': float(r_band_mag_str)}, ignore_index=True)
          elif(spec_type_str[0] == 'B'):
              print(str(row['Object']) + ": " + spec_type_str[0:temp_sense] + ' Type Blue Massive Star') #Can you print the OBject as well
              spectral_bins[1] += 1
              if(spec_type_str[1] == '0' or spec_type_str[1] == '1' or spec_type_str[1] == '2' or spec_type_str[1] == '3'):
                  spectral_bins_temp[3] += 1  
              elif(spec_type_str[1] == '4' or spec_type_str[1] == '5' or spec_type_str[1] == '6'):
                  spectral_bins_temp[4] += 1    
              elif(spec_type_str[1] == '7' or spec_type_str[1] == '8' or spec_type_str[1] == '9'):
                  spectral_bins_temp[5] += 1
              if(isinstance(r_band_mag_str, str)):
                  print("Magnitude: " + str(r_band_mag_str))
                  magnitude_spec_type = magnitude_spec_type.append({'Object': str(row['Object']), 
                                                                    'Category': str(row['Category']),
                                                                    'Spec_Type':str(spec_type_str[0:2]),
                                                                    'Magnitude': float(r_band_mag_str)}, ignore_index=True)
          elif(spec_type_str[0] == 'A'):
              print(str(row['Object']) + ": " + spec_type_str[0:temp_sense] + ' Type Blue Dwarf Star') #Can you print the OBject as well
              spectral_bins[2] += 1
              if(spec_type_str[1] == '0' or spec_type_str[1] == '1' or spec_type_str[1] == '2' or spec_type_str[1] == '3'):
                  spectral_bins_temp[6] += 1  
              elif(spec_type_str[1] == '4' or spec_type_str[1] == '5' or spec_type_str[1] == '6'):
                  spectral_bins_temp[7] += 1    
              elif(spec_type_str[1] == '7' or spec_type_str[1] == '8' or spec_type_str[1] == '9'):
                  spectral_bins_temp[8] += 1
              if(isinstance(r_band_mag_str, str)):
                  print("Magnitude: " + str(r_band_mag_str))
                  magnitude_spec_type = magnitude_spec_type.append({'Object': str(row['Object']), 
                                                                    'Category': str(row['Category']),
                                                                    'Spec_Type':str(spec_type_str[0:2]),
                                                                    'Magnitude': float(r_band_mag_str)}, ignore_index=True)
          elif(spec_type_str[0] == 'F'):
              print(str(row['Object']) + ": " + spec_type_str[0:temp_sense] + ' Type Yellow-white Dwarf Star') #Can you print the OBject as well
              spectral_bins[3] += 1
              if(spec_type_str[1] == '0' or spec_type_str[1] == '1' or spec_type_str[1] == '2' or spec_type_str[1] == '3'):
                  spectral_bins_temp[9] += 1  
              elif(spec_type_str[1] == '4' or spec_type_str[1] == '5' or spec_type_str[1] == '6'):
                  spectral_bins_temp[10] += 1    
              elif(spec_type_str[1] == '7' or spec_type_str[1] == '8' or spec_type_str[1] == '9'):
                  spectral_bins_temp[11] += 1
              if(isinstance(r_band_mag_str, str)):
                  print("Magnitude: " + str(r_band_mag_str))
                  magnitude_spec_type = magnitude_spec_type.append({'Object': str(row['Object']), 
                                                                    'Category': str(row['Category']),
                                                                    'Spec_Type':str(spec_type_str[0:2]),
                                                                    'Magnitude': float(r_band_mag_str)}, ignore_index=True)
          elif(spec_type_str[0] == 'G'):
              print(str(row['Object']) + ": " + spec_type_str[0:temp_sense] + ' Type Yellow Dwarf Star') #Can you print the OBject as well        
              spectral_bins[4] += 1
              if(spec_type_str[1] == '0' or spec_type_str[1] == '1' or spec_type_str[1] == '2' or spec_type_str[1] == '3'):
                  spectral_bins_temp[12] += 1  
              elif(spec_type_str[1] == '4' or spec_type_str[1] == '5' or spec_type_str[1] == '6'):
                  spectral_bins_temp[13] += 1    
              elif(spec_type_str[1] == '7' or spec_type_str[1] == '8' or spec_type_str[1] == '9'):
                  spectral_bins_temp[14] += 1
              if(isinstance(r_band_mag_str, str)):
                  print("Magnitude: " + str(r_band_mag_str))
                  magnitude_spec_type = magnitude_spec_type.append({'Object': str(row['Object']), 
                                                                    'Category': str(row['Category']),
                                                                    'Spec_Type':str(spec_type_str[0:2]),
                                                                    'Magnitude': float(r_band_mag_str)}, ignore_index=True)
          elif(spec_type_str[0] == 'K'):
              print(str(row['Object']) + ": " + spec_type_str[0:temp_sense] + ' Type Orange Dwarf Star') #Can you print the OBject as well        
              spectral_bins[5] += 1
              if(spec_type_str[1] == '0' or spec_type_str[1] == '1' or spec_type_str[1] == '2' or spec_type_str[1] == '3'):
                  spectral_bins_temp[15] += 1  
              elif(spec_type_str[1] == '4' or spec_type_str[1] == '5' or spec_type_str[1] == '6'):
                  spectral_bins_temp[16] += 1    
              elif(spec_type_str[1] == '7' or spec_type_str[1] == '8' or spec_type_str[1] == '9'):
                  spectral_bins_temp[17] += 1
              if(isinstance(r_band_mag_str, str)):
                  print("Magnitude: " + str(r_band_mag_str))
                  magnitude_spec_type = magnitude_spec_type.append({'Object': str(row['Object']), 
                                                                    'Category': str(row['Category']),
                                                                    'Spec_Type':str(spec_type_str[0:2]),
                                                                    'Magnitude': float(r_band_mag_str)}, ignore_index=True)
          elif(spec_type_str[0] == 'M'):
              print(str(row['Object']) + ": " + spec_type_str[0:temp_sense] + ' Type Red Dwarf Star') #Can you print the OBject as well
              spectral_bins[6] += 1
              if(spec_type_str[1] == '0' or spec_type_str[1] == '1' or spec_type_str[1] == '2' or spec_type_str[1] == '3'):
                  spectral_bins_temp[18] += 1  
              elif(spec_type_str[1] == '4' or spec_type_str[1] == '5' or spec_type_str[1] == '6'):
                  spectral_bins_temp[19] += 1    
              elif(spec_type_str[1] == '7' or spec_type_str[1] == '8' or spec_type_str[1] == '9'):
                  spectral_bins_temp[20] += 1
              if(isinstance(r_band_mag_str, str)):
                  print("Magnitude: " + str(r_band_mag_str))
                  magnitude_spec_type = magnitude_spec_type.append({'Object': str(row['Object']), 
                                                                    'Category': str(row['Category']),
                                                                    'Spec_Type':str(spec_type_str[0:2]),
                                                                    'Magnitude': float(r_band_mag_str)}, ignore_index=True)

  return (missing_spectral_class,spectral_bins, spectral_bins_temp, magnitude_spec_type)

def sort_mag(data):
#visualize by magnitude of the catalog!
  missing_mag = 0
  object_magnitude = pd.DataFrame(columns=['Object', 'Category' ,'Magnitude']) #empty pandas array

  for index, row in data.iterrows():
      r_band_mag_str = row['R_band_mag']
      #print(type(r_band_mag_str))
      if (isinstance(r_band_mag_str, float)): #the nan got treated as a float
          #print(str(row['Object']) + " " + str(r_band_mag_str))
          missing_mag+=1
      else:
          if(r_band_mag_str != '-'):
              #print(str(row['Object']) + ": " + str(r_band_mag_str)) #Can you print the OBject as well
              object_magnitude = object_magnitude.append({'Object': str(row['Object']), 
                                                          'Category' : str(row['Category']),
                                                          'Magnitude': float(r_band_mag_str)}, ignore_index=True)
          else:
              missing_mag+=1
        
  return (missing_mag, object_magnitude)

def sort_magnitude_spec_type_arrange(magnitude_spec_type, spectral_types , spectral_types_bins):
  magnitude_spec_type_arrange = pd.DataFrame(columns=['Object', 
                                                    'Categrory',
                                                    'Spec_Type',
                                                    'Magnitude',]) #empty pandas array

  magnitude_spec_type_bins_arrange = pd.DataFrame(columns=['Object', 
                                                      'Categrory',
                                                      'Spec_Type',
                                                      'Magnitude',]) #empty pandas array
  #you can also count how many don't have magnitude and valild spectral types
  for types in spectral_types: #O, B, A, F, G, K, M
      for index, row in magnitude_spec_type.iterrows():
          if(row['Spec_Type'][0] == types): #if spectral type is same as type
              magnitude_spec_type_arrange = magnitude_spec_type_arrange.append({'Object': str(row['Object']),
                                                                                'Categrory':  str(row['Category']),
                                                                                'Spec_Type': str(row['Spec_Type']),
                                                                                'Magnitude': float(row['Magnitude'])}, 
                                                                               ignore_index=True)

  for types in spectral_types_bins: #O B A F G K M, This is redundant now
      for index, row in magnitude_spec_type.iterrows():     
          if(row['Spec_Type'][0] == types[0] and
             int(row['Spec_Type'][1]) >= int(types[1]) and #in the bins but
             int(row['Spec_Type'][1]) <= int(types[3])): #Ther are some cases with Class 0,
              #something happened in the sorting process, soemthing is wrong
              magnitude_spec_type_bins_arrange = magnitude_spec_type_bins_arrange.append({'Object': str(row['Object']),
                                                                                          'Categrory':  str(row['Category']),
                                                                                          'Spec_Type': str(row['Spec_Type']),
                                                                                          'Magnitude': float(row['Magnitude'])}, 
                                                                                           ignore_index=True)

  t = np.array(magnitude_spec_type_bins_arrange)

  p = [[] for i in range(len(spectral_types))]
  #make an array slice
  q = 0
  for i in range(0, len(magnitude_spec_type_bins_arrange)-1):
      p[q].append(t[i])
      if(magnitude_spec_type_bins_arrange['Spec_Type'][i+1][0] != magnitude_spec_type_bins_arrange['Spec_Type'][i][0]):
          q +=1

  p[q].append(t[186])

  for v in range(0,len(p)):
      n = len(p[v])
      #bubble sort
      for i in range(n):
              # Last i elements are already in place
          for j in range(0, n-i-1):
              if p[v][j][2] > p[v][j+1][2] :
                  p[v][j][2], p[v][j+1][2] = p[v][j+1][2], p[v][j][2]

  column_names =["Object", "Category", 'Spec_Type','Magnitude']
  final_dataframe = pd.DataFrame(columns = column_names)
  final_dataframe

  for t in p: #for lists in p
      for g in t: #for objects in list
          a_series = pd.Series(g, index = final_dataframe.columns)
          final_dataframe = final_dataframe.append(a_series, ignore_index=True)

  mean_magnitude_spec_class = []
  mean_magnitude_spec_class.append(0)
  for z in range(0 , len(spectral_types)-1):
    mean_magnitude_spec_class.append(np.mean(np.array(p[z])[:,3]))

  return (magnitude_spec_type_arrange, final_dataframe, mean_magnitude_spec_class)
