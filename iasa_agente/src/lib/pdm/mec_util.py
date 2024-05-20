class MecUtil():
    
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
        
    def utilidade(self):
        S = self.__modelo.S
        A = self.__modelo.A

        U = {s: 0 for s in S()}

        while True:
            Uant = U.copy()
            delta = 0

            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))

            if delta <= self.__delta_max:
                break

        return U
    
    def util_accao(self, s, a, U):
        T = self.__modelo.T
        R = self.__modelo.R
        gama = self.__gama

        return sum(T(s, a, sn) * (R(s, a, sn) + gama * U[sn]) for sn in self.__modelo.S())