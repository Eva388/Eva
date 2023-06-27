This folder contains all the files of the tribometer research.

It contains the following folders:
-Baseline:
  This has the data on the Stribeck curves for water on a specific subtrate. It has data for glass,steel and PDMS

-Exported Data:
  This contains the raw exported data from the Tribometer. We exported all data by selecting all data sets related to one setup
  (solution + substrate) and then exporting as CSVs. This was repeated for all setups.

-Tribometer Data Analysis:
  This folder contains the notebooks used for analyzing the data that was exported. There is a separate subfolder (DATA) which is used to 
  store the data that should be analyzed. This folder expects it in a setup as follows: DATA -> SURFACTANT -> CONCENTRATION -> Datasets.
  These datasets are not the raw sets from the "Exported Data" folder, they are first cleaned with the processing script found in the 
  "Tribometer_processing_package" folder.

-Tribometer Prototypes:
  This folder contains the first prototypes that were created for the processing script. These should not be used but were included for
  completeness.

-Tribometer_processing_package
  This folder contains the processing script used to clean up the raw data sets found in the "Exported Data" folder. A single raw dataset
  should be put into into the "RAW" subfolder. If the script "Processing.py" is then executes it will create cleaned datasets and put this in
  the "CSV" subfolder. This data should be copied to an appropriate folder in the "DATA" folder of the "Tribometer Data Analysis" folder.
  It is possible that the "config.py" script needs to be modified first for this to work

-Visco:
  This contains data on the viscosity. There are two notebooks. One used for analysis to see wheter the fluids are Newtonian or non-Newtonian. The other 
  notebook is summary which was used to get the mean viscosity value for the analysis "Tribometer Data Analysis". The VISC_list file contains lists that are 
  copied into the code in the 
