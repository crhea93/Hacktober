"""
Read in galaxy zoo information for galaxies from the AGN host galaxies sample found here at their site
https://data.galaxyzoo.org/?_ga=2.7190002.1970643156.1592065564-2043771608.1592065564
The input file name is schawinski_GZ_2010_catalogue.fits

This will read in the GZ information, initiate the Galaxy classes for each galaxy, then save in pickle
"""

from astropy.io import fits
from ClassGalaxy import Galaxy
from astropy.table import Table
from tqdm import tqdm
import gc
import sqlite3

import multiprocessing
from joblib import Parallel, delayed

#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#

#---------------------------------------------------------------------------------------------------#
conn = sqlite3.connect('SDSS_ratios.sql')
cursor = conn.cursor()

# Read in fits table
GZ_catalog = fits.open('schawinski_GZ_2010_catalogue.fits')
catalog = Table(GZ_catalog[1].data)
# The data is stored as individual arrays where each element represents a different galaxy
# We will pull the arrays for the OBJID and Category
Redshift = catalog['REDSHIFT'][0]
ObjID = catalog['OBJID'][0]
Morphology = catalog['GZ1_MORPHOLOGY'][0]
BPT_class = catalog['BPT_CLASS'][0]
RA = catalog['RA'][0]
DEC = catalog['DEC'][0]
# Run parallelized for loop
num_cores = 1#multiprocessing.cpu_count()-2
inputs = tqdm(range(len(ObjID[11:12])))
#Parallel(n_jobs=num_cores, verbose=0)(delayed(add_galaxy)(i)for i in inputs)
# Save Galaxies to file using pickle
#with open('Galaxy_ratio.csv', "w+") as f:
    #f.write('SDSS_ID, CAT, r1, r2 , r3, r4\n')
for gal_ct in inputs:
    id_ = ObjID[gal_ct]
    redshift_ = Redshift[gal_ct]
    morph_ = Morphology[gal_ct]
    bpt_ = BPT_class[gal_ct]
    ra_ = RA[gal_ct+1]
    dec_ = DEC[gal_ct+1]
    # Initiate Galaxy
    galaxy_ = Galaxy(id_, morph_, bpt_, ra_, dec_)
    galaxy_.download_and_save_image()  # Get spectrum



    del galaxy_
