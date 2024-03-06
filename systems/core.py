# import cosapp
from cosapp.base import System, Port

class Core(System):

    def __init__(self, name,*arg):
        self.port_in = Port
        self.port_out = Port
        super().__init__(name,*arg)
        
    def setup(self):
        self.add_inward('Vcpu')
        self.add_outward('Wcpu')

        self.add_input(self.port_in,'p_in')
        self.add_output(self.port_out,'p_out')

    def compute(self):
        self.Wcpu = 100*self.Vcpu
        

