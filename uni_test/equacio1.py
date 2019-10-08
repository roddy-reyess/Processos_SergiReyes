class equacio1:
    def __init__(self, equacio):
        self.s_eq = equacio
    def calcula(self):
        calculante = self.s_eq.split()
        tuX = calculante[0]
        tuX = tuX.replace(tuX[-1],'')
        tuX = float(tuX)
        finalnum = float(calculante[-1])
        num2 = float(calculante[2])
        if calculante[1] == "+":
            respuesta = (finalnum - num2) / tuX
        elif calculante[1] == "-":
            respuesta = (finalnum + num2) / tuX
        return "x " + "= " + str(respuesta)
