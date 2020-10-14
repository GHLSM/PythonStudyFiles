import abc
class All_file(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass
    @abc.abstractmethod
    def write(self):
        pass

class Cdrom(All_file):
    def read(self):
        print('ok')
    def write(self):
        print('ok')

class Rom(All_file):
    def read(self):
        pass

R1=Rom()
