from controlo_react.controloReact import ControloReact
from controlo_react.reaccoes.aproximar.aproximarAlvo import AproximarAlvo
from controlo_react.reaccoes.evitar.evitarObst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from sae.agente.agente import Agente
from sae.simulador import Simulador


class AgenteReact(Agente):
    
    def __init__(self):
        controlo = ControloReact(Recolher([Explorar(), AproximarAlvo(), EvitarObst()]))
        controlo.mostrar_per_dir = True
        super().__init__(controlo)
        
if __name__ == "__main__":
    Simulador(1, AgenteReact()).executar()