# CitraBounds

This repository contains code to reproduce simulations related to enhancing the accuracy of genome-scale metabolic models by incorporating kinetic information. The included files and scripts are used to analyze the updated *E. coli* metabolic model, iML1515, evaluating dormant reactions, flux flexibility, and other key parameters.

## Repository Contents

1. **`dead_reac_func.py`**: Includes utility functions to:
   - Count dormant reactions.
   - Assess uncertainty (flux flexibility) after applying kinetic constraints.
   - Generate cumulative distributions.

2. **`graphs_nocitra_FUN_sup.py`**: Runs simulations and generates visualizations for:
   - Dormant reactions vs. the number of implemented kinetic constraints.
   - Variability in reaction fluxes.
   - Comparisons between original and kinetically constrained models.

3. **`fba_dead_reac_original_proof_rev2_nocitra_FUNexp.py`**: The core simulation script. It integrates the iML1515 model and applies kinetic constraints based on the the steady state simulation of the kinetic model. It includes functionality for:
   - Flux Balance Analysis (FBA) optimization.
   - Flux Variability Analysis (FVA).
   - Iterative implementation of kinetic constraints.

4. **Metabolic Model**: The model used is `iML1515.xml`.

## Prerequisites

1. **Python Dependencies**:
   - `cobra`
   - `numpy`
   - `matplotlib`
   - `pandas`

   Install them using:
   ```bash
   pip install cobra numpy matplotlib pandas
   ```

2. **Kinetic Flux File**:
   Include an Excel file (`kinetic_fluxes.xls`) containing kinetic flux values used to apply constraints.

## Execution

### 1. Initial Setup
Ensure the metabolic model file (`iML1515.xml`) and kinetic data file (`kinetic_fluxes.xls`) are in the same directory as the scripts.

### 2. Main Simulation
Run the main script to simulate metabolic optimization:
```bash
python3 graphs_nocitra_FUN_sup.py
```

This script:
- Calls simulation functions in `fba_dead_reac_original_proof_rev2_nocitra_FUNexp.py`.
- Produces visualizations comparing results between the original and kinetically constrained models.

### 3. Analyze Results
The following graphs are generated:
- Cumulative distribution of flux flexibility.
- Number of dormant reactions after applying constraints.
- Comparison of growth rates and metabolic variability.

## Methodology

1. **Metabolic Model**:
   - The iML1515 model is used, representing *E. coli*'s metabolic reactions.
   - A fixed glucose flux is applied as a substrate.

2. **Kinetic Constraints**:
   - Kinetic fluxes are derived from the kinetic model in `E_coli_Millard2016.xml`.
   - Lower and upper bounds are applied to key reactions.

3. **Results Analysis**:
   - The impact of kinetic constraints is evaluated on dormant reactions and flux flexibility.
