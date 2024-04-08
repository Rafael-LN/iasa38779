from controlo_react.controloReact import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from sae.agente.agente import Agente
from sae.simulador import Simulador


class AgenteReact(Agente):
    
    def __init__(self):
        controlo = ControloReact(Recolher([Explorar()]))
        super().__init__(controlo)
        
if __name__ == "__main__":
    Simulador(1, AgenteReact()).executar()