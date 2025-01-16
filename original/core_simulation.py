simport cobra
# import cobra.test
import xlwt
from cobra.flux_analysis import flux_variability_analysis
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
from metrics_fun import dead_reactions_count, uncertainty, uncertainty_second_part, cumulative_distr


xls = pd.ExcelFile(r"kinetic_fluxes.xls")
sheetX = xls.parse(0)
col_1 = sheetX['reaction flux [mM h-1]']
# col_2 = sheetX['Vmax']
# print(col_1[1])


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
		 'ACONTa',
		 'ACONTb',
		 'ICDHyr',
		 'AKGDH',
		 'SUCOAS',
		 'SUCDi',
		 'FUM']  # Añadir MDH2 cuando ub y lb son 1.3 y 0.7
		 
 
 
 
C = 6.372  # Units conversion constant
g = 0.23  # glucose flux in the kinetic model in mmol gdw-1 h-1
l_int = 0.7  # lower uncertainty constant
u_int = 1.3  # upper uncertainty constant
tkt1_f = 0.0133798062183819   # kinetic flux for TKT1
tkt2_f = 0.0132904547198724   # kinetic flux for TKT2
tala_f = 0.0133798063281831   # kinetic flux for TALA 

def core_sim(stoich_reactions, g, tkt1_f, tkt2_f, tala_f, l_int =[], u_int=[]):

    # Load model and set the initial glucose and growth rate constraints

    # const_model = cobra.io.read_sbml_model("MODEL1108160000.xml")
    const_model = cobra.io.read_sbml_model("iML1515.xml")
    const_model.solver = 'cplex'
    const_model.objective = 'BIOMASS_Ec_iML1515_WT_75p37M'
    gluc_fluxmin = const_model.reactions.get_by_id("EX_glc__D_e").lower_bound = -C*g # *1000
    gluc_fluxmax = const_model.reactions.get_by_id("EX_glc__D_e").upper_bound = -C*g # *1000


    solutions = []  # list that contains the solutions for the citramalate production after the implementation of each reaction bounds
    # dead_reac = []

    flux_kin = []  # list with the kinetic fluxes extracted from the excel file
    dead_reac = [] # list with the count of dead reactions adter the implementation of each reaction boudns
    flex = [] # empty list that will contain the diference between minimum and maximum fluxes after FVA. This one is for the initial condition
    

    # Simulation and adding the initial solution without added bounds to the solutions list

    solution = const_model.optimize()
    solutions.append(solution.objective_value)
    print(solutions)

    # FVA simulation

    fva_sim = flux_variability_analysis(const_model, const_model.reactions, fraction_of_optimum=0.999)
    mini = list(fva_sim.minimum)
    maxi = list(fva_sim.maximum)
    dead_reactions_count(mini, maxi, dead_reac, 1e-2)
    uncertainty(mini, maxi, flex)
    # print(flex)

    # for i in col_1:
    #    flux_kin.append(i)

    flux_kin = col_1

    # print(reac_id, flux_kin)

    # Uncertainty

    less_flex_rxns = []
    more_flex_rxns = []

    for z, l in zip(stoich_reactions[:15], flux_kin[:17]):
        
            flex_new = []
            lim_rxns = 0
            aug_rxns = 0
            
            # print(flux_variability_analysis(const_model, const_model.reactions.get_by_id(z))) # COMMENT THIS TO NOT KILL THE PROCESS
      
            
            if z == 'PGK' or z == 'PGM' or z == 'RPI':
                # try:
                    # lb = const_model.reactions.get_by_id(k).lower_bound = -C*m
                    lb = const_model.reactions.get_by_id(z).lower_bound = -C*l*u_int
                    ub = const_model.reactions.get_by_id(z).upper_bound = -C*l*l_int
                # except Exception as e:
                    # math.inf
                    
            elif z == 'TKT1':
                # try:
                    lb = const_model.reactions.get_by_id(z).lower_bound = C*tkt1_f*l_int
                    ub = const_model.reactions.get_by_id(z).upper_bound = C*tkt1_f*u_int
                    # ub = const_model.reactions.get_by_id(k).upper_bound = 1000
                    # math.inf
                    
            elif z == 'TKT2':
                # try:
                    lb = const_model.reactions.get_by_id(z).lower_bound = C*tkt2_f*l_int
                    ub = const_model.reactions.get_by_id(z).upper_bound = C*tkt2_f*u_int
                # except Exception as e:
                    # math.inf
                    
            elif z == 'TALA':
                # try:
                    lb = const_model.reactions.get_by_id(z).lower_bound = C*tala_f*l_int
                    ub = const_model.reactions.get_by_id(z).upper_bound = C*tala_f*u_int
                    # ub = const_model.reactions.get_by_id(k).upper_bound = 1000
                # except Exception as e:
                    # math.inf	
            else:
                # try:
                    lb = const_model.reactions.get_by_id(z).lower_bound = C*l*l_int
                    ub = const_model.reactions.get_by_id(z).upper_bound = C*l*u_int				
                    # ub = const_model.reactions.get_by_id(k).upper_bound = C*m
                # except Exception as e:
                    # math.inf	
            solution = const_model.optimize()
            solutions.append(solution.objective_value)
            print(solutions)
            print('z flux: ', const_model.reactions.get_by_id(z).flux)
            fva_sim = flux_variability_analysis(const_model, const_model.reactions, fraction_of_optimum=0.999)
            mini = list(fva_sim.minimum)
            maxi = list(fva_sim.maximum)
            
            # print('Bounds: ', lb, ub)
            # print(flux_variability_analysis(const_model, const_model.reactions.get_by_id(z)))
            # Dead reactions and uncertainty count
            
            dead_reactions_count(mini, maxi, dead_reac, 1e-2)
            uncertainty(mini, maxi, flex_new)
            uncertainty_second_part(flex, flex_new, lim_rxns, aug_rxns, less_flex_rxns, more_flex_rxns, 1e-2)
            
            # print(flex[43], flex_new[43])
    
    # print(stoich_reactions[17:], flux_kin[17:])
    
    for z, l in zip(stoich_reactions[15:], flux_kin[19:]): # change here to [15:] and [19:] 
        
            flex_new = []
            lim_rxns = 0
            aug_rxns = 0
            
            # print(flux_variability_analysis(const_model, const_model.reactions.get_by_id(z))) # COMMENT THIS TO NOT KILL THE PROCESS
            
            if z == 'SUCOAS' or z == 'MDH':
                # try:
                    # lb = const_model.reactions.get_by_id(k).lower_bound = -C*m
                    lb = const_model.reactions.get_by_id(z).lower_bound = -C*l*u_int
                    ub = const_model.reactions.get_by_id(z).upper_bound = -C*l*l_int
                    
            else:
                lb = const_model.reactions.get_by_id(z).lower_bound = C*l*l_int
                ub = const_model.reactions.get_by_id(z).upper_bound = C*l*u_int	
                                
            solution = const_model.optimize()
            solutions.append(solution.objective_value)
            print(solutions)
            print('z flux: ', const_model.reactions.get_by_id(z).flux)
            fva_sim = flux_variability_analysis(const_model, const_model.reactions, fraction_of_optimum=0.999)
            mini = list(fva_sim.minimum)
            maxi = list(fva_sim.maximum)
                    
            # Dead reactions and uncertainty count
                    
            dead_reactions_count(mini, maxi, dead_reac, 1e-2)
            uncertainty(mini, maxi, flex_new)
            uncertainty_second_part(flex, flex_new, lim_rxns, aug_rxns, less_flex_rxns, more_flex_rxns, 1e-2)
                    
                    
    
    # cumulative_distr(flex, flex_new)
    cdf2 = cumulative_distr(flex, flex_new)
    print(cdf2)
    print(solutions)
    print(dead_reac)
    print(less_flex_rxns, more_flex_rxns)
    print(const_model.reactions.get_by_id('FBP').upper_bound)
    print(const_model.reactions.get_by_id('FBP').lower_bound)
    print(const_model.reactions.get_by_id('CS').upper_bound)
    print(const_model.reactions.get_by_id('CS').lower_bound)
    print(const_model.reactions.get_by_id('ACONTa').upper_bound)
    print(const_model.reactions.get_by_id('ACONTa').lower_bound)
    print(const_model.reactions.get_by_id('ACONTb').upper_bound)
    print(const_model.reactions.get_by_id('ACONTb').lower_bound)
    # print(const_model.reactions.get_by_id('MDH2').upper_bound)
    # print(const_model.reactions.get_by_id('MDH2').lower_bound)
    return solutions, dead_reac, less_flex_rxns, more_flex_rxns, flex, flex_new
    
    
# core_sim(stoich_reactions, g, tkt1_f, tkt2_f, tala_f, l_int =0.9, u_int=1.1)
