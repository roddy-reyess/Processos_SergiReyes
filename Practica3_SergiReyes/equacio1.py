class equacio1:
    def __init__(self, equacio):
        self.s_eq = equacio
        self.calculante = self.s_eq.split()
        self.tuX = 0.0
        self.num2 = 0.0
        self.finalnum = 0.0
        self.respuesta = 0.0
    def calcula(self):
        if not self.s_eq:
            return "l'equacio no segueix el format: ax + b = c"
        elif("x" in self.calculante[0]):

            self.tuX = self.calculante[0]
            self.tuX = self.tuX.replace(self.tuX[-1],'')
            self.tuX = float(self.tuX)

            self.finalnum = float(self.calculante[-1])

            try:
                float(self.calculante[2])
            except:
                return "l'equacio conte caracter no calculables: "+self.s_eq

            self.num2 = float(self.calculante[2])

            if self.calculante[1] == "+":
                self.respuesta = (self.finalnum - self.num2) / self.tuX
                self.respuesta = float("{0:.2f}".format(self.respuesta))

            elif self.calculante[1] == "-":
                self.respuesta = (self.finalnum + self.num2) / self.tuX
                self.respuesta = float("{0:.2f}".format(self.respuesta))

            else:
                self.respuesta = "Error " + self.calculante[1]
            return self.respuesta
        else:
            return "l'equacio no segueix el format: ax + b = c"
