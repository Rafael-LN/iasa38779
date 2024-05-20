class MecUtil():
    
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
        
    def utilidade(self):
        S = self._modelo.S
        A = self._modelo.A
        U = {s: 0 for s in S()}

        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta <= self._delta_max:
                break

        return U
    
    def util_accao(self, s, a , U):
        return sum(self._modelo.T(s, a, sn) * (self._modelo.R(s, a, sn) + self._gama * U[sn]) for sn in self._modelo.S())