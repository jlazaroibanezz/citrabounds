# citrabounds

The provided .py files can be used to reproduce the simulation results of the paper: "Enhancing the accuracy of genome-scale metabolic models with kinetic information". The attached folders 'original' and 'citramax' hold the code for the original model of E. Coli and for the citramalate-producing model respectively.

## Methodology

The methodology is only explained for the original model, but works similarly for the citramalate-producing model.

- Download the E. coli genome-scale metabolic model MODEL1108160000 from: https://www.ebi.ac.uk/biomodels/MODEL1108160000
- Donwload the files contained in the folder 'original'.
- Once imported all the libraries required in the script, run in your terminal the following command:

```
$ python3 graphs_nocitra_FUN.py
```
This file calls back the functions in the other present files that run the simulation to obtain the Flux Balance Analysis solutions and all the complementary metrics evaluated in the paper.
