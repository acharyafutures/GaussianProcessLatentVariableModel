import qml
from qml.kernels import gaussian_kernel
from qml.math import cho_solve

import os
import numpy as np

import matplotlib.pyplot as plt

import natsort

#Splitting data into smaller files of each molecule
def file_splitter(filename,foldername):
    lines_per_file=14
    file_piece=None
    count = 0 
    with open(filename) as data_file:
        for count, line in enumerate(data_file):
            if count % lines_per_file==0:
                if file_piece:
                    file_piece.close()
                new_filename=foldername+'/file_{}.txt'.format(count)
                file_piece=open(new_filename,"w")
            file_piece.write(line)
        if file_piece:
            file_piece.close()
            
#loading output in .dat to np array
def load_output(filename):
    #opening energies as output_training_data
    fw=open(filename,"r")
    out_lines=fw.read().splitlines()
    fw.close()
    y=np.array(out_lines)
    return y


# Converting each file to qml format and making coulomb matrix
def compounds(foldername):
    compounds=[qml.Compound(xyz=foldername+"/"+f) for f in natsort.natsorted(os.listdir(foldername+"/"))]
    for mol in compounds:
        mol.generate_coulomb_matrix(size=12)
    return compounds
