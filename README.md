# RNAconcentrationField
This repository contains Python scripts for analyzing and comparing experimental and modeled RNA concentration data. The models and data sets referenced here are based on work from ChemRxiv.

Table of Contents
Overview
Figure 2
Figure 3
Figure 5
Figure 6

Overview
This repository includes multiple Python scripts—each dedicated to generating figures (or sets of figures) and performing specific analyses. Various data files (e.g., .txt, .npy, .pkl) accompany these scripts to provide both experimental measurements and corresponding model outputs.

_____Figure 2_____
Files
Fig2.py: Main script to generate Figure 2.
Fig2_data2D.txt: Model data for creating the 2D plot.
Fig2_data_line.txt: Model data for the line plot.

Description
Figure 2 compares experimental data with a theoretical model using 2D visualizations and line plots.
python Fig2.py
This script will read Fig2_data2D.txt and Fig2_data_line.txt, then generate Figure 2 as displayed in the repository’s documentation.
![fig2](https://github.com/user-attachments/assets/ad9c1b93-d917-432b-8b7e-4ff136e988dc)

_____Figure 3_____
Files
Fig3.py: Main script to generate Figure 3c.
Fig3_data.txt: Model data for creating the 2D figure.

Description
Figure 3c demonstrates a comparison of experimental data with a model for the concentration profiles.
python Fig3.py
This script will read Fig3_data.txt and generate Figure 3c.
![fig3](https://github.com/user-attachments/assets/37d9c8be-1c44-4df3-a81f-86fc591e4aff)

_____Figure 5_____
Files
Fig5.py: Main script to generate Figure 5f.
Fig5_data.pkl: Experimental data file.
Fig5_model_O, Fig5_model_X, Fig5_model_clov, Fig5_model_fitted_pat, Fig5_model_random, Fig5_model_single: Model data files.
Fig5_modeling_convolution_v1.py: Script for performing convolution-based modeling.

Description
Figure 5f visualizes both experimental data and results from various modeled conditions.
Fig5.py uses Fig5_data.pkl and multiple Fig5_model_* data files to generate plots of experimental and modeled RNA concentration distributions.
Fig5_modeling_convolution_v1.py performs convolution calculations for the modeling approach.
python Fig5.py
This will read the appropriate data files, generate Figure 5f, and display the comparison of models.
![fig5](https://github.com/user-attachments/assets/024da061-f42f-4246-87ec-de87a9d982b6)

_____Figure 6_____
Files
Fig6.py: Main script to generate Figures 5g, 5i, and 5j (sometimes referred to as parts of “Figure 6” in the text).
Fig6_data.npy: Experimental data file.
Fig6_model.npy: Model data file.
Fig6_optimization_algorithm.py: Script for running the optimization loop to produce Figures 6b, 6c, 6d.
Fig6_target_pattern.npy: The target pattern that the optimization algorithm tracks and mimics.
Description
Fig6.py uses Fig6_data.npy and Fig6_model.npy to generate the specified panels (5g, 5i, and 5j) comparing experimental and modeled data.
Fig6_optimization_algorithm.py reads Fig6_target_pattern.npy and performs the iterative optimization to reproduce Figures 6b, 6c, and 6d.
python Fig6.py
python Fig6_optimization_algorithm.py
![fig6_DW](https://github.com/user-attachments/assets/e457ca79-d81d-42e2-8770-0d5da5947ff9)

_____Dependencies and Usage_____
Python Version: Ensure you are using Python 3.7+ (or a recent Python 3 release).
Libraries: Typical scientific Python stack (NumPy, Matplotlib, possibly Pandas).
Example installation command:
bash
Copy code
pip install numpy matplotlib pandas
Running the Scripts:
In the terminal or command prompt, navigate to the repository directory.
Execute the scripts with python <script_name>.py.
