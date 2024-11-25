class Ahorcado():

    palabra = ''
    vidas = 6
    letrasUsadas = []
    palabraescondida = ''

    def __init__(self, palabraInicial):
        self.reset(palabraInicial)
        #self.setVidas(6)
        #self.definirPalabra(palabraInicial)
        #self.setLetrasUsadas([])
        #self.getPalabraEscondida =   " ".join(["_" for x in self.getPalabra()])
        #self.setPalabraEscondida('')

    def pruebaLetra(self,letra):
        if (not(self.fueUsada(letra))):
            mensaje = self.verificarLetra(letra)
            self.letrasUsadas.append(letra)
            if (self.getPalabraEscondida().replace(' ', '') == self.getPalabra()):
                mensaje = 'GANASTE'
            return mensaje
        else:
            return 'USADA'

    def verificarLetra(self, a):
        posi = self.getPalabra().find(a)
        if (posi != -1):
            self.setPalabraEscondida(a)
            return 'CORRECTA'
        else:
            self.restarVida()
            if (self.getVidas() == -1):
                return 'PERDISTE'
            else :
                return 'INCORRECTA'
        
    def verificarPalabra(self, a): 
        if (self.getPalabra() == a):
            return 'GANASTE'
        else:
            return 'PERDISTE'
    
    def restarVida(self):
        self.vidas -= 1

    def definirPalabra(self, x):
        self.palabra = x
    
    def getPalabra(self):
        return self.palabra
    
    def setVidas(self,x):
        self.vidas = x
   
    def fueUsada(self,letra):
        try:
            posicion = self.getLetrasUsadas().index(letra)
            return True
        except ValueError:
            return False
        
    def getPalabraEscondida(self):
        return self.palabraescondida
    
    
    def setPalabraEscondida(self, letra):
        self.palabraescondida = ' '.join([i if (i == letra or self.getPalabraEscondida().find(i)!=-1) else "_" for i in self.getPalabra()])

    def setLetrasUsadas(self,x):
        self.letrasUsadas = x
    
    def getLetrasUsadas(self):
        return self.letrasUsadas
    
    def getVidas(self):
        return self.vidas

    def reset(self, palabra=''):
        self.setVidas(6)
        self.definirPalabra(palabra)
        self.setLetrasUsadas([])
        self.setPalabraEscondida('')