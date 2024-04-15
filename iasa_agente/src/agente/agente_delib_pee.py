from sae.agente.agente import Agente
from sae.simulador import Simulador


class AgenteDelibPee(Agente):
    def __init__(self):
        super().__init__(controlo) #TODO: implementação será realizada mais tarde
        
if __name__ == "__main__":
    Simulador(1, AgenteDelibPee()).executar()