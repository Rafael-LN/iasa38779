from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPEE
from sae.agente.agente import Agente
from sae.simulador import Simulador


class AgenteDelibPee(Agente):
    def __init__(self):
        super().__init__(ControloDelib(PlaneadorPEE()))
        
if __name__ == "__main__":
    Simulador(4, AgenteDelibPee()).executar()