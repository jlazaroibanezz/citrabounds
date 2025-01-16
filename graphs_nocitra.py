import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from  core_simulation import core_sim 


 
''' 
stoich_reactions = ['PGI',  # list of reactions whose kinetic bounds are being translated
 'PFK',
 'FBA',
 'TPI',
 'GAPD',
 'PGK',
 'PGM',
 'ENO',
 'PYK',
 'G6PDH2r',
 'PGL',
 'GND',
 'RPE',
 'RPI',
 'TKT1',
 'FBP',
 'PPC',
 'PPCK',
 'PPS',
 'ME1',
 'PDH',
 'CS',
 'ACONTa']
 '''
 
stoich_reactions_1 = ['PGI',  # list of reactions whose kinetic bounds are being translated
		 'PFK',
		 'FBA',
		 'TPI',
		 'GAPD',
		 'PGK',
		 'PGM',
		 'ENO',
		 'PYK',
		 'G6PDH2r',
		 'PGL',
		 'GND',
		 'RPE',
		 'RPI',
		 'TKT1',
		 'FBP',
		 'PPC',
		 'PPCK',
		 'PPS',
		 'ME1',
		 'PDH',
		 'CS',
		 'ACONTa',
		 'ACONTb',
		 'ICDHyr',
		 'AKGDH',
		 'SUCOAS',
		 'SUCDi',
		 'FUM']  # Añadir MDH2 cuando ub y lb son 1.3 y 0.7
		 
		 
stoich_reactions_2 = ['PGI',  # list of reactions whose kinetic bounds are being translated
		 'PFK',
		 'FBA',
		 'TPI',
		 'GAPD',
		 'PGK',
		 'PGM',
		 'ENO',
		 'PYK',
		 'G6PDH2r',
		 'PGL',
		 'GND',
		 'RPE',
		 'RPI',
		 'TKT1',
		 'FBP',
		 'PPC',
		 'PPCK',
		 'PPS',
		 'ME1',
		 'PDH',
		 'CS',
		 'ACONTa',
		 'ACONTb',
		 'ICDHyr',
		 'AKGDH',
		 'SUCOAS',
		 'SUCDi',
		 'FUM'] # ,
		 # 'MDH2']  # Añadir MDH2 cuando ub y lb son 1.3 y 0.7
		 
x_1 = ['No reactions', 'PGI',  # list of reactions whose kinetic bounds are being translated
	 'PFK',
	 'FBA',
	 'TPI',
	 'GAPD',
	 'PGK',
	 'PGM',
	 'ENO',
	 'PYK',
	 'G6PDH2r',
	 'PGL',
	 'GND',
	 'RPE',
	 'RPI',
	 'TKT1',
	  'FBP',
	 'PPC',
	 'PPCK',
	 'PPS',
	 'ME1',
	 'PDH',
	 'CS',
	 'ACONTa',
	 'ACONTb', 
	 'ICDHyr',
	 'AKGDH',
	 'SUCOAS',
	 'SUCDi',
	 'FUM'] #,
	 # 'MDH2']
	 
x_2 = ['No reactions', 'PGI',  # list of reactions whose kinetic bounds are being translated
	 'PFK',
	 'FBA',
	 'TPI',
	 'GAPD',
	 'PGK',
	 'PGM',
	 'ENO',
	 'PYK',
	 'G6PDH2r',
	 'PGL',
	 'GND',
	 'RPE',
	 'RPI',
	 'TKT1',
	  'FBP',
	 'PPC',
	 'PPCK',
	 'PPS',
	 'ME1',
	 'PDH',
	 'CS',
	 'ACONTa',
	 'ACONTb',
	 'ICDHyr',
	 'AKGDH',
	 'SUCOAS',
	 'SUCDi',
	 'FUM'] #,
	 # 'MDH2']
	
h_1 = ['PGI',  # list of reactions whose kinetic bounds are being translated
	 'PFK',
	 'FBA',
	 'TPI',
	 'GAPD',
	 'PGK',
	 'PGM',
	 'ENO',
	 'PYK',
	 'G6PDH2r',
	 'PGL',
	 'GND',
	 'RPE',
	 'RPI',
	 'TKT1',
	  'FBP',
	 'PPC',
	 'PPCK',
	 'PPS',
	 'ME1',
	 'PDH',
	 'CS',
	 'ACONTa',
	 'ACONTb',
	 'ICDHyr',
	 'AKGDH',
	 'SUCOAS',
	 'SUCDi',
	 'FUM'] 
	 
h_2 = ['PGI',  # list of reactions whose kinetic bounds are being translated
 'PFK',
 'FBA',
 'TPI',
 'GAPD',
 'PGK',
 'PGM',
 'ENO',
 'PYK',
 'G6PDH2r',
 'PGL',
 'GND',
 'RPE',
 'RPI',
 'TKT1',
  'FBP',
 'PPC',
 'PPCK',
 'PPS',
 'ME1',
 'PDH',
 'CS',
 'ACONTa',
 'ACONTb',
 'ICDHyr',
 'AKGDH',
 'SUCOAS',
 'SUCDi',
 'FUM'] #
 # , 'MDH2']

 
C = 6.372  # Units conversion constant
g = 0.23  # glucose flux in the kinetic model in mmol gdw-1 h-1
l_int = [0.9, 0.94, 0.97]  # lower uncertainty constant
u_int = [1.1, 1.06, 1.03]  # upper uncertainty constant
tkt1_f = 0.0133798062183819   # kinetic flux for TKT1
tkt2_f = 0.0132904547198724   # kinetic flux for TKT2
tala_f = 0.0133798063281831   # kinetic flux for TALA 

flexibility_cumdist = []
flexibility_cumdist_2 = []
flexibility_cumdist_3 = []
flexibility_cumdist_4 = []

for count, (o, p) in enumerate(zip(l_int, u_int)):
	if o == 0.7 and p == 1.3:
		stoich_reactions = stoich_reactions_2 ### 2
		x = x_2
		h = h_2
	
	else: 
		stoich_reactions = stoich_reactions_1
		x = x_1
		h = h_1
	 	
	solutions, dead_reac, less_flex_rxns, more_flex_rxns, flex, flex_new = core_sim(stoich_reactions, g, tkt1_f, tkt2_f, tala_f, l_int = o, u_int = p)

	# NO CITRAMALATE

	# 30%
	
	
	
	x = range(0, len(x))
	# x = [0, len(x)]

	y = dead_reac

	fig, ax = plt.subplots(figsize=(12, 8))
	ax2=ax.twinx()

	# ax.set_xticks(np.arange(len(x))) ###
	ax.plot(x,y, color="#E73E3E",marker="o", markersize = 7)
	ax.set_xlabel('Number of kinetic bounds implemented', fontsize = 24)
	ax.set_ylabel('Number of dormant reactions', color="#E73E3E", fontsize=24)
	ax.tick_params(axis="y", labelcolor="#E73E3E", labelsize = 20)
	ax.tick_params(axis="x", labelsize = 20)
	ax.set_ylim(1000, 2200) # 1750, 1950

	y2 = solutions    

	# twin object for two different y-axis on the sample plot

	# make a plot with different y-axis using second axis object
	ax2.plot(x, y2,color="#236BA1",marker="^", markersize = 7, label = 'FBA solution')
	ax2.set_ylabel('Growth rate $h^{-1}$' , color="#236BA1", fontsize=20)
	ax2.tick_params(axis="y", labelcolor="#236BA1", labelsize = 20)
	plt.ylim(0, max(y2)+0.05)

	# plt.gca().legend(('Dead reactions','y1'))

	plt.show()

	# FLEXIBILITY
	
 
	h = range(1, len(h)+1)
	# x = [1, len(x)+1]

	# NO CITRA

	# 30%

	y1 = less_flex_rxns
	y2 =  more_flex_rxns
	print('Here', len(h), len(y1), len(y2))

	fig, ax = plt.subplots(figsize=(12,8))
	# ax.set_xticks(np.arange(len(x)+1)) ###
	ax.plot(h,y1, marker = 'o', markersize = 7, color='#FF7A33', label = 'Decreased variability')
	ax.plot(h,y2, marker = '^', markersize = 7, color='#33C1FF', label = 'Increased variability')
	ax.legend(fontsize = 20)
	ax.set_xlabel('Number of kinetic bounds implemented', fontsize = 24)
	ax.set_ylabel('Number of reactions', fontsize = 24)
	ax.tick_params(axis="y", labelsize = 20)
	ax.tick_params(axis="x", labelsize = 20)
	# ax.set_ylim(0, 1400)
	ax.set_ylim(0, 1400) # 0, 200
	
	plt.show()

	# Dead reactions vs growth rate

	x = dead_reac

	y = solutions

	fig, ax = plt.subplots(figsize=(12, 8))
	# ax2=ax.twinx()

	ax.scatter(x,y, color="black",marker="o")
	ax.set_ylabel('Growth rate $h^{-1}$' , color="#236BA1", fontsize=20)
	ax.set_xlabel('Number of dormant reactions', color="black", fontsize=20)
	ax.tick_params(axis="y", labelcolor="black", labelsize = 14)
	ax.tick_params(axis="x", labelsize = 12)

	plt.show()
	
	'''
	if flex not in flexibility_cumdist:
		flexibility_cumdist.append(flex)
	flexibility_cumdist.append(flex_new)
	print(len(flexibility_cumdist))
	'''
	flexibility_cumdist.append(flex)
	print(count)
	
	if count == 0:
		flexibility_cumdist_2.append(flex_new)
	if count == 1:
		flexibility_cumdist_3.append(flex_new)
	if count == 2:
		flexibility_cumdist_4.append(flex_new)
	

count, bins_count = np.histogram(flexibility_cumdist[0], bins=1000000)
pdf = count / sum(count)
cdf = np.cumsum(pdf)
count2, bins_count2 = np.histogram(flexibility_cumdist_2[0], bins=1000000)
pdf2 = count2 / sum(count2)
cdf2 = np.cumsum(pdf2)
count3, bins_count3 = np.histogram(flexibility_cumdist_3[0], bins=1000000)
pdf3 = count3 / sum(count3)
cdf3 = np.cumsum(pdf3)
count4, bins_count4 = np.histogram(flexibility_cumdist_4[0], bins=1000000)
pdf4 = count4 / sum(count4)
cdf4 = np.cumsum(pdf4)

# print('dist1', distribution_1)
# print('dist2', distribution_2)
# plt.plot(bins_count[1:], pdf, color="red", label="PDF")
plt.plot(bins_count[1:], cdf, label="Original model")
plt.plot(bins_count[1:], cdf2, label="Kinetically constrained d=0.03")
plt.plot(bins_count[1:], cdf3, label="Kinetically constrained d=0.06")
plt.plot(bins_count[1:], cdf4, label="Kinetically constrained d=0.1")
plt.xscale("log")
plt.xlabel("FV (mmol $g_{DW}^{-1}$ $h^{-1}$)")
plt.ylabel("Proportion of reacions")
plt.title('Cumulative distribution')
plt.legend()
plt.show()


    
