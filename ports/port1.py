from cosapp.ports import Port

class Port1(Port):
    def setup(self):
        self.add_variable('x', 0.)