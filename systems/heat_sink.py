from cosapp.base import System, Port

class HeatSink(System):

    def setup(self):

        self.add_inward('spec_heat', 895., unit='J/kg/K', desc='Aluminium specific heat')
        self.add_inward('area', 0.45, unit='m**2')
        self.add_inward('volume', 0.185, unit='m**3')
        self.add_inward('mass', 0.5, unit='kg')
        self.add_inward('emissivity', 0.2)
        
        self.add_inward('airspeed', 0., unit='m/s')
        
        self.add_inward('convection_coeff', 10., unit='W/m/m/K')
        self.add_inward('interface_conduction', 10., unit='W/m/K')
        self.add_inward('interface_thickness', 0.01, unit='m')
        self.add_inward('Tcpu', 300., unit='K')
        self.add_inward('Troom', 292., unit='K')
        self.add_inward('T', 291., unit='K')

        self.add_outward('cooling_power', 0.0, unit='W')
        self.add_outward('dT',0., unit='K/s')

        self.add_transient('T', der='dT')

    def compute(self):

        v = self.airspeed
        hcW = 12.12 - 1.16*v + 11.6*v**(1/2)
        thermal_paste_conductivity = 8. # W/m/K
        boltzmann_constant = 5.670373E-8
        self.cooling_power = (thermal_paste_conductivity/self.interface_thickness)*(self.Tcpu - self.T)
        self.dT = (self.cooling_power - hcW*self.area*(self.T - self.Troom))/(self.spec_heat*self.mass)
        
        # self.dT = self.cooling_power/(self.spec_heat*self.mass)
        # self.dT = self.dT - self.area*boltzmann_constant*self.emissivity*(self.T**4-self.Troom**4)/(self.spec_heat*self.mass)


