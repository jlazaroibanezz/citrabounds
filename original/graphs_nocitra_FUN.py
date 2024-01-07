import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from  fba_dead_reac_original_proof_rev2_nocitra_FUNexp import core_sim 

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
 'TKT2',
 'TALA',
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
 'FUM'
 ,'MDH2']
 
 
C = 6.372  # Units conversion constant
g = 0.23  # glucose flux in the kinetic model in mmol gdw-1 h-1
l_int = 0.7  # lower uncertainty constant
u_int = 1.3  # upper uncertainty constant
tkt1_f = 0.0112695236047172  # kinetic flux for TKT1
tkt2_f = 0.00565509193942248  # kinetic flux for TKT2
tala_f = 0.011269523604676  # kinetic flux for TALA

solutions, dead_reac, less_flex_rxns, more_flex_rxns = core_sim(stoich_reactions, g, l_int, u_int, tkt1_f, tkt2_f, tala_f)

# NO CITRAMALATE

# 30%


x = ['No reactions', 'PGI',  # list of reactions whose kinetic bounds are being translated
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
 'TKT2',
 'TALA',
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
 'FUM'
 , 'MDH2']


x = range(0, len(x))


y = dead_reac

fig, ax = plt.subplots(figsize=(12, 8))
ax2=ax.twinx()

# ax.set_xticks(np.arange(len(x))) ###
ax.plot(x,y, color="#E73E3E",marker="o", markersize = 7)
ax.set_xlabel('Added Reaction', fontsize = 24)
ax.set_ylabel('Number of dead reactions', color="#E73E3E", fontsize=24)
ax.tick_params(axis="y", labelcolor="#E73E3E", labelsize = 20)
ax.tick_params(axis="x", labelsize = 20)


y2 = solutions     

# twin object for two different y-axis on the sample plot

# make a plot with different y-axis using second axis object
ax2.plot(x, y2,color="#236BA1",marker="^", markersize = 7, label = 'FBA solution')
ax2.set_ylabel('Growth rate $h^{-1}$' , color="#236BA1", fontsize=24)
ax2.tick_params(axis="y", labelcolor="#236BA1", labelsize = 20)
plt.ylim(0, max(y2)+0.05)

# plt.gca().legend(('Dead reactions','y1'))

plt.show()

# FLEXIBILITY

x = ['PGI',  # list of reactions whose kinetic bounds are being translated
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
 'TKT2',
 'TALA',
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
 'FUM'
 , 'MDH2']

x = range(1, len(x)+1)

# NO CITRA

# 30%

y1 = less_flex_rxns
y2 =  more_flex_rxns

fig, ax = plt.subplots(figsize=(12,8))
# ax.set_xticks(np.arange(len(x)+1)) ###
ax.plot(x,y1, marker = 'o', markersize = 7, color='mediumorchid', label = 'Decreased variability')
ax.plot(x,y2, marker = '^', markersize = 7, color='dodgerblue', label = 'Increased variability')
ax.legend(fontsize= 20)
ax.set_xlabel('Added Reaction', fontsize = 24)
ax.set_ylabel('Number of reactions', fontsize = 24)
ax.tick_params(axis="y", labelsize = 20)
ax.tick_params(axis="x", labelsize = 20)

plt.show()

# Dead reactions vs growth rate

x = dead_reac

y = solutions

fig, ax = plt.subplots(figsize=(12, 8))
# ax2=ax.twinx()

ax.scatter(x,y, color="black",marker="o")
ax.set_ylabel('Growth rate ($h^{-1}$)', fontsize = 20)
ax.set_xlabel('Number of dead reactions', color="black", fontsize=20)
ax.tick_params(axis="y", labelcolor="black", labelsize = 14)
ax.tick_params(axis="x", labelsize = 12)

plt.show()



