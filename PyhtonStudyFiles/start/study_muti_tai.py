class H2O:
    def __init__(self,state,tem):
        self.state=state
        self.tem=tem
    def state_change(self):
        if self.tem < 0:
            print('%s在环境温度为%s℃的情况下，为冰' %(self.state,self.tem))
        elif self.tem > 0 and self.tem < 100:
            print('%s在环境温度为%s℃的情况下，为水' %(self.state,self.tem))
        elif self.tem > 100:
            print('%s在环境温度为%s℃的情况下，为蒸汽' %(self.state,self.tem))

class water(H2O):
    pass
class ice(H2O):
    pass
class gas(H2O):
    pass

ice1=ice('冰',50)
ice1.state_change()
