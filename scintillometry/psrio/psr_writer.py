"""psr_writer.py defines the writer class for writing the scintillometry data
results to a self-describable file.
"""

import astropy.units as u
from astropy.time import Time



__all__ = ['HDUwriter']




class HDUwriter:
    def __init__(self, HDU_translator):
        self.translator = HDU_translator
        self.hdu_type = self.translator.client_name

    def 