import numpy as np
import matplotlib.pyplot as plt

'''
Function to calculate the number of dead reactions.
Parameters:
- minimum: minimum flux after the FVA
- maximum: maximum flux after de FVA
- dead_reac: empty list to add the number of dead reactions after each kinetic bounds translation
- epsilon: threshold flux to consider that a reaction is dead
'''

def dead_reactions_count(minimum, maximum, dead_reac, epsilon):
    deadcount = 0
    for i, j in zip(minimum, maximum):
        if abs(i) <= epsilon and abs(j) <= epsilon:
            deadcount += 1
            
    dead_reac.append(deadcount)
    
'''
Function to add to a list the difference between the minimum and maximum FVA fluxes.
Parameters:
- minimum: minimum flux after the FVA
- maximum: maximum flux after de FVA
- flexibility: empty list to add the difference after each kinetic bounds translation
'''        
    
def uncertainty(minimum, maximum, flexibility):
    for i, j in zip(minimum, maximum):
        if (i < 0 and j >= 0) or (i >= 0 and j > 0) or (i == 0 and j == 0): 
            interval_dif = j-i
            flexibility.append(interval_dif)
            
        elif i < 0 and j < 0:
            interval_dif = abs(j-abs(i))
            flexibility.append(interval_dif)
        
'''
Function to calculate the number of reactions that reduce and increase their flux range 
Parameters:
- flex: list having the fluxes range for the model without constraints added (control)
- flex_new: list having the fluxes range for the model with constraints added (each iteration)
- lim_rxns: initialized at 0, counts the number of reactions that reduced their range after implementing the kinetic bounds in each iteration
- aug_rxns: initialized at 0, counts the number of reactions that increased their range after implementing the kinetic bounds in each iteration
- less_flex_rxns: empty list to add the numbers in lim_rxns after implementing the kinetic bounds in each iteration
- more_flex_rxns: empty list to add the numbers in aug_rxns after implementing the kinetic bounds in each iteration

'''         
        
def uncertainty_second_part(flex, flex_new, lim_rxns, aug_rxns, less_flex_rxns, more_flex_rxns, epsilon):
        for i, j in zip(flex, flex_new):
            if i > (j + epsilon):
                lim_rxns += 1
            elif i < (j - epsilon):
                aug_rxns += 1

        less_flex_rxns.append(lim_rxns)
        more_flex_rxns.append(aug_rxns)

def cumulative_distr(distribution_1, distribution_2): # introduce in this case, flex and flex_new
    count, bins_count = np.histogram(distribution_1, bins=10000000)
    pdf = count / sum(count)
    cdf = np.cumsum(pdf)
    count2, bins_count2 = np.histogram(distribution_2, bins=10000000)
    pdf2 = count2 / sum(count2)
    cdf2 = np.cumsum(pdf2)
    # plt.plot(bins_count[1:], pdf, color="red", label="PDF")
    plt.plot(bins_count[1:], cdf, label="Original model")
    plt.plot(bins_count[1:], cdf2, label="Kinetically constrained model")
    plt.xscale("log")
    plt.xlabel("FV (mmol $g_{DW}^{-1}$ $h^{-1}$)")
    plt.ylabel("Proportion of reacions")
    plt.title('Cumulative distribution')
    plt.legend()
    plt.show()
