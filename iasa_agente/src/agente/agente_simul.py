from sae import Agente, Simulador
from controlo_simul.controlo_simul import ControloSimul

class AgenteSimul(Agente):
    
    def __init__(self):
        controlo = ControloSimul()
        super().__init__(controlo)
        
        
if __name__ == "__main__":
    Simulador(1, AgenteSimul()).executar()
    