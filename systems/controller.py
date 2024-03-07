from cosapp.base import System, Port

class Controller(System):

    # def __init__(self, name,*arg):
    #     self.port_in = Port
    #     self.port_out = Port
    #     super().__init__(name,*arg)
        
    def setup(self):
        
        self.add_inward('Tcpu', 292., unit='K')
        self.add_outward('Vfan', 0., unit='V')

        # self.add_input(self.port_in,'p_in')
        # self.add_output(self.port_out,'p_out')

    def compute(self):
        if self.Tcpu > 313.:
            self.Vfan = 6. # Volts
        if self.Tcpu > 333.:
            self.Vfan = 12. # Volts

        

