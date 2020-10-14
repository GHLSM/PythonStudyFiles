import time
class Open:
    def __init__(self,filename,mode='r',encoding='utf-8'):
        # self.filename=filename
        self.file=open(filename,mode,encoding=encoding)
        self.mode=mode
        self.encoding=encoding
    def  write(self,line):
        t=time.strftime('%Y-%m-%d-%X')
        self.file.write('%s %s' %(t,line))
    def __getattr__(self, item):
        print(item)
        # self.file.read()
        return getattr(self.file,item)
    # def read(self):
    #     pass
    # def write(self):
    #     pass
f1=Open('a.txt','w+')
print(f1.read)
f1.write('运载\n')
f1.write('CPU\n')
