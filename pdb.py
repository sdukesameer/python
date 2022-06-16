class pdb:
    x=0
    def __init__(self,n):
        self.x=n
    def party(self):
        self.x=self.x+1
        print("So far",self.x)
    def __del__(self):
        print("bye")
class new(pdb):
    p=0
    def t(self):
        self.p=self.p+7
        self.party()
        print(self.p)
an=new(25)
an.party()
an.t()
an.party()
print(type(an))
print(dir(an))