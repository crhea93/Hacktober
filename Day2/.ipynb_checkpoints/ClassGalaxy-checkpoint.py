"""
Each galaxy is considered an instance of the galaxy class. The class contains three key pieces of information:
1 - SDSS DR7 ID
2 - Pointer to Spectrum
3 - Galaxy Zoo Classification
"""

from astroquery.sdss import SDSS
from astropy import units as u
from astropy import coordinates as coords
import matplotlib.pyplot as plt
import numpy as np


class Galaxy:
    """
    """
    def __init__(self, SDSS_id, galaxy_classification, galaxy_morphology, ra, dec):
        self.sdss_id = SDSS_id
        self.galaxy_classification = galaxy_classification  # BPT classification
        self.galaxy_morphology = galaxy_morphology  # Galaxy morphology
        self.ra = ra  # Coordinate in J2000
        self.dec = dec  # Coordinate in J2000
        self.line_fluxes = []  # [ha, n1, n2, s1, s2]
        self.ratios = []  # [r1, r2, r3 , r4]


    def __str__(self):
        return "ID: %s"%self.sdss_id

    def download_and_save_image(self):
        pos = coords.SkyCoord(ra=self.ra*u.degree, dec= self.dec*u.degree, frame='fk5')
        img = SDSS.get_images(self.sdss_id, band='g')[0]
        print(pos)
        print(img[0])
        img.writeto('test.fits', overwrite=True)
