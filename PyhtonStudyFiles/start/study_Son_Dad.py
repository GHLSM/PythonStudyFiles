# class Vehicle:
#     Conuntry='China'
#     def __init__(self,name,speed,load,power):
#         self.name=name
#         self.speed=speed
#         self.load=load
#         self.power=power
#     def run(self):
#         print('run')
# class Metro(Vehicle):
#     def __init__(self,name,speed,load,power,line):
#         self.name = name
#         self.speed = speed
#         self.load = load
#         self.power = power
#         self.line = line
#     def show_info(self):
#         print(self.name,self.line)
#
# line1=Metro('武汉Metro line','40km/h',1000000,'Elc',1)
# line1.show_info()
#
#
# class Vehicle:
#     Conuntry='China'
#     def __init__(self,name,speed,load,power):
#         self.name=name
#         self.speed=speed
#         self.load=load
#         self.power=power
#     def run(self):
#         print('run')
# class Metro(Vehicle):
#     def __init__(self,name,speed,load,power,line):
#         Vehicle.__init__(self,name,speed,load,power)
#         self.line = line
#     def show_info(self):
#         print(self.name,self.line)
#
# line1=Metro('武汉Metro line','40km/h',1000000,'Elc',1)
# line1.show_info()
#
# class Vehicle:
#     Conuntry='China'
#     def __init__(self,name,speed,load,power):
#         self.name=name
#         self.speed=speed
#         self.load=load
#         self.power=power
#     def run(self):
#         print('run')
# class Metro(Vehicle):
#     def __init__(self,name,speed,load,power,line):
#         super().__init__(name,speed,load,power)
#         self.line = line
#     def show_info(self):
#         super().run()
#         print(self.name,self.line)
#
# line1=Metro('武汉Metro line','40km/h',1000000,'Elc',1)
# line1.show_info()
