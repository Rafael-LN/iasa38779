from agente.controlo_react.controlo_react import ControloReact
from agente.controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from agente.controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from sae.agente.agente import Agente
from sae.simulador import Simulador


class AgenteReact(Agente):
    
    def __init__(self):
        controlo = ControloReact(Recolher([AproximarAlvo(), EvitarObst(), Explorar()]))
        controlo.mostrar_per_dir = True
        super().__init__(controlo)
        
if __name__ == "__main__":
    Simulador(1, AgenteReact()).executar()