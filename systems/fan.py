from cosapp.base import System, Port

class Fan(System):

    def setup(self):

        self.add_inward('Vfan', 0., unit='V')
        self.add_inward('diameter', 0.12, unit='m')
        self.add_outward('airspeed', 0., unit='m/s')

    def compute(self):
        # 100 CFM = 0.05 m**3/s
        pi = 3.14159
        area = pi*(self.diameter/2)**2
        self.airspeed = (0.05/10)*self.Vfan/area
        
        

