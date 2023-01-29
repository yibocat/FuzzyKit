import numpy as np

from .FuzzyNums import Fuzzynum


class qrungfn(Fuzzynum):

    def __init__(self, qrung, md, nmd):
        super().__init__()
        md = np.asarray(md)
        nmd = np.asarray(nmd)
        self.qrung = qrung
        assert ((md.size == 0 or md.size == 1) and (
                nmd.size == 0 or nmd.size == 1) and 0 <= md <= 1 and 0 <= nmd <= 1) and 0 <= md ** qrung + nmd ** qrung <= 1, \
            'ERROR: Both of MD and NMD and MD^q+NMD^q must have be in the interval[0,1] and the number of MD or NMD must have be 1.'
        self.md = md
        self.nmd = nmd

    def __repr__(self):
        return 'QRungFN(Q=%d):(' % self.qrung + '\n' + '    md: ' + str(
            np.around(self.md, 4)) + '\n' + '    nmd:' + str(
            np.around(self.nmd, 4)) + ')'

    def isLegal(self):
        """
            Checks if the Q-Rung fuzzy number is legal.
        """
        assert ((self.md.size == 0 or self.md.size == 1) and
                (self.nmd.size == 0 or self.nmd.size == 1) and 0 <= self.md <= 1 and 0 <= self.nmd <= 1) \
               and 0 <= self.md ** self.qrung + self.nmd ** self.qrung <= 1, 'ERROR: Illegal Q-rung fuzzy number!'
