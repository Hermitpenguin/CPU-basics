from cosapp.base import System, Port

class Controller(System):      

    def setup(self):

        self.add_inward('Tcpu', 292., unit='K')
        self.add_outward('Vfan', 0., unit='V')

    def compute(self):
        self.Vfan = 0.
        if self.Tcpu > 333.:
            self.Vfan = 6. # Volts
        if self.Tcpu > 353.:
            self.Vfan = 12. # Volts