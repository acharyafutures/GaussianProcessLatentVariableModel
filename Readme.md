
## Gaussian Process Latent Variable Model for Improved sampling of molecular trajectories in molecular Machine Learning


### File structure
The file is on the following tree format
```
.
├── Readme.md
├── requirements.txt
└── Thesis_Code
    ├── DFTB_splitted
    ├── MD_splitted
    ├── noise_splitter
    ├── predicted_splitted_data
    ├── test_data_II
    ├── xyz_files
    │   ├── c6h6.xyz
    │   └── energies_benzene.xyz
    ├── extract_excited_energy.sh
    ├── run1.sh
    ├── test.xyz.inp
    ├── functions_utils.py
    ├── regression_function.py
    ├── gplvm.ipynb
    ├── Benchmarking.ipynb
    ├── ORCA_and_predicted_splitter.ipynb
    ├── regression_implementation.ipynb
    └── xyz_pred.ipynb
```

```Readme.md``` is the file currently opened and that you are in.```requirements.txt``` consists the packages used in this code.```Thesis_Code``` folder consists the implementation as well as the data of the code. The actual data are not kept in this project, their file structure is only the representation.




### Installation 

You can install those packages with

```bash
  pip install -r requirements.txt
```
    
### Implementation

The folder Thesis_Code consists of different folders as

```
    ├── DFTB_splitted
    ├── MD_splitted
    ├── noise_splitter
    ├── predicted_splitted_data
    ├── test_data_II
    ├── xyz_files
        ├── c6h6.xyz
        └── energies_benzene.xyz

```
**DFTB_splitted**, **MD_splitted**, **noise_splitter**, **predicted_splitted_data** contains the files having just one molecule in each of them, which are automatically created when running the code. 
**You need to create these folders manually before running the code**.

**xyz_files** contains the molecular trajectories, where initially molecular trajectory and its energies should be kept.
Make sure to adjust the file name as in tree above. While running the code trajectory of 1 million molecules with name noise_xyz and trajectory of predicted molecules with name predicted_xyz will also be added.
### ORCA

These are the files required to run the ORCA for predicting molecular energies. These files are the bash script and .inp file. They are automatically executed while running the code.

```
    ├── extract_excited_energy.sh
    ├── run1.sh
    ├── test.xyz.inp

```

### Python Files
Please read the comments above the every code block(if exists) of every .ipynb files before you run it.

```functions_utils.py``` and ```regression_function.py``` contains the functions that are being called by different jupyter notebooks. functions_utils.py contains splitting trajectory to each file and converting those files to Coulomb matrix.

```regression_implementation.ipynb``` is the jupyter notebook in which the baseline experiment is done.

```Benchmarking.ipynb``` is the jupyter notebook in which the benchmarking experiment is done. 

```gplvm.ipynb``` is the jupyter notebook in which converting high dimension data into low dimension, predicting new points in latent space and finally conversion of those new points to Coulomb matrix is done. When running this file a file name ```predicted_coulomb_matrix.npy``` will be created.

```xyz.pred``` is the jupyter notebook in which bayesian optimisation is implemented and predicted_coulomb_matrix is mapped to molecules with 1 million added noise.

```ORCA_and_predicted_splitter``` is the jupyter notebook in which the predicted trajectory is splitted and ORCA is run for computation of energies.When running this file a file name ```energies_from_predicted.npy``` will be created.

You need to pull this entire content keep initial trajectory and its energies in 'c6h6.xyz' and 'energies_benzene.xyz' respectively inside 'xyz_files' folder. Further, you need to have new similar trajectories for benchmarking inside 'test_data_II' folder, and update its path in ```Benchmarking.ipynb```.
Then you can run the regression_implementation, gplvm, xyz_pred, ORCA_and_predicted_splitter and Benchmarking ipynb files. You will get various plots while running those files. The predicted molecular trajectory will be inside xyz_files with name of predicted_xyz.xyz and it's splitted form in folder named predicted_splitted_data.
