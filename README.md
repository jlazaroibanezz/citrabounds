# CitraBounds

This repository contains code to reproduce simulations related to enhancing the accuracy of genome-scale metabolic models by incorporating kinetic information. We parted from a genome-scale and a kinetic model of *E. coli*:
- The [iML1515](http://bigg.ucsd.edu/models/iML1515) model from BiGG Models is a genome-scale metabolic model of Escherichia coli str. K-12 MG1655. It includes 1516 genes, 2712 reactions, and 1877 metabolites, representing a comprehensive reconstruction of the organism's metabolism. This model serves as a robust tool for simulating metabolic fluxes, predicting growth rates under various conditions, and exploring genetic modifications for biotechnological and research applications.
- The [E_coli_Millard2016.xml](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005396) model captures the main central carbon pathways and accounts for 68 reactions and 77 metabolites which are located in 3 compartments: environment, periplasm and cytoplasm. The model represents glucose-limited conditions and is expressed as a set of ordinary differential equations.

Both models were modified adding the reactions necessary for citramalate synthesis (see paper "Enhancing Genome-Scale Metabolic Models with Kinetic Data: Resolving Growth and Citramalate Production Trade-offs in *E. coli*").
The included files and scripts were used to analyze the updated apply the information of the kinetic model to the genome-scale metabolic model in both situations (original and citramalate-producing scenarios). We evaluated flux metrics such as dormant reactions, flux variability, and other key parameters. 

 Only the steps of the procedure for the non-producing citramalate model (original) are displayed but the same process should be applied for the "citramax" directory.

## Repository Contents

1. **`metrics_fun.py`**: Includes utility functions to:
   - Count dormant reactions.
   - Assess uncertainty (flux flexibility) after applying kinetic constraints.
   - Generate cumulative distributions.

2. **`graphs_nocitra.py`**: Runs simulations and generates visualizations for:
   - Dormant reactions vs. the number of implemented kinetic constraints.
   - Variability in reaction fluxes.
   - Comparisons between original and kinetically constrained models.
   - `graphs_with_citra.py` is utilized in the citramalate-producing scenario.

3. **`core_simulation.py`**: The core simulation script. It integrates the iML1515 model and applies kinetic constraints based on the the steady state simulation of the kinetic model. It includes functionality for:
   - Flux Balance Analysis (FBA) optimization.
   - Flux Variability Analysis (FVA).
   - Iterative implementation of kinetic constraints.

4. **Metabolic Model**: The model used is `iML1515.xml`. Replaced with `iML1515CITRA.xml` in the citramalate-producing scenario.

## Prerequisites

1. **Python Requisites**:
   - `cobra`
   - `numpy`
   - `matplotlib`
   - `pandas`
   - `xlwt`
   - `xlrd`

   Install them using:
   ```bash
   pip install cobra numpy matplotlib pandas xlwt xlrd
   ```

2. **Kinetic Flux File**:
   Include an Excel file (`kinetic_fluxes.xls`) containing kinetic flux values used to apply constraints.

## Execution

### 1. Initial Setup
Ensure the metabolic model file (`iML1515.xml`) and kinetic data file (`kinetic_fluxes.xls`) are in the same directory as the scripts.

### 2. Main Simulation
Run the main script to simulate metabolic optimization:
```bash
python3 graphs_nocitra.py
```

This script:
- Calls simulation functions in `core_simulation.py`.
- Produces visualizations comparing results between the original and kinetically constrained models.

### 3. Analyze Results
The following graphs are generated:
- Cumulative distribution of flux variability.
- Number of dormant reactions after applying constraints.
- Comparison of growth rates and metabolic variability.

## Methodology

1. **Metabolic Model**:
   - The iML1515 model is used, representing *E. coli*'s metabolic reactions.
   - A fixed glucose flux is applied as a substrate.

2. **Kinetic Constraints**:
   - Kinetic fluxes are derived from the kinetic model in `E_coli_Millard2016.xml` which was simulated until steady state was reached giving the fluxes of `kinetic_fluxes.xls`
   - Lower and upper bounds are applied to key reactions.

3. **Results Analysis**:
   - The impact of kinetic constraints is evaluated on dormant reactions and flux variability.

## Solvers

Before running the simulations, it is essential to have installed a linear programming solver. In this work we used [CPLEX](https://www.ibm.com/es-es/products/ilog-cplex-optimization-studio), but others such as [GLPK](https://www.gnu.org/software/glpk/) and [Gurobi](https://www.gurobi.com/) are supported as well.

To easily install GLPK:

```bash
     sudo apt-get install python-glpk
     sudo apt-get install glpk-utils
```
