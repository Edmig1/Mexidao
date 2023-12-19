class Revelacao_Do_Acesso_Do_Usuario(object):
    def __init__(self, initval=None, name ='var'):
        self.val = initval
        self.name = name
    def __get__(self, obj, objtype):
        print('Recuperando', self.name)
        return self.val

    def __set__(self, obj, val):
        print('Atualizando', self.name)
        self.val = val
class vossaclasse(object):
    x = Revelacao_Do_Acesso_Do_Usuario(10, 'var "x')
    y = 5
m = vossaclasse()
print('x: ', m.x)
m.x=20
print('x: ', m.x)
print('y: ', m.y)
m.y=8
print('y: ', m.y)