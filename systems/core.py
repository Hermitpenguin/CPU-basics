from cosapp.base import System, Port

class Core(System):

    # def __init__(self, name,*arg):
    #     self.port_in = Port
    #     self.port_out = Port
    #     super().__init__(name,*arg)
        
    def setup(self):
        self.add_inward('vcpu', 0., unit='V')
        self.add_inward('spec_heat', 710., unit='J/kg/K', desc='Silicon specific heat')
        self.add_inward('mass', 0.06, unit='kg')
        self.add_inward('Troom', 293.)

        self.add_outward('wcpu', unit='W')
        self.add_outward('dT', unit='K/s')

        self.add_transient('T', der='dT')

        # self.add_input(Port1,'p_in')
        # self.add_output(Port1,'p_out')

    def compute(self):
        self.wcpu = 100*self.vcpu
        boltzmann_constant = 5.670373E-8
        self.dT = self.wcpu/(self.spec_heat*self.mass) - 0.05*0.05*boltzmann_constant*0.2*(self.T**4-self.Troom**4)/(self.spec_heat*self.mass)

