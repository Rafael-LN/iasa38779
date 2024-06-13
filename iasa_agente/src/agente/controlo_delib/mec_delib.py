from sae.ambiente.elemento import Elemento


class MecDelib():
    """
    Classe que representa um mecanismo de deliberação.

    Atributos:
        __modelo_mundo (objeto): O modelo de mundo utilizado para a deliberação.

    Métodos:
        __init__: Inicializa um mecanismo de deliberação com o modelo de mundo fornecido.
        deliberar: Delibera sobre o estado atual do mundo e retorna uma lista de possíveis estados futuros.
        gerar_objectivos: Gera os objetivos com base no estado atual do mundo.
        seleccionar_objectivos: Seleciona os objetivos a serem perseguidos com base nos objetivos gerados.
    """

    def __init__(self, modelo_mundo):
        """
        Inicializa um mecanismo de deliberação com o modelo de mundo fornecido.

        Argumentos:
            modelo_mundo: O modelo de mundo utilizado para a deliberação.
        """
        self.__modelo_mundo = modelo_mundo
        
    def deliberar(self):
        """
        Delibera sobre o estado atual do mundo e retorna uma lista de possíveis estados futuros.

        Retorno:
            Uma lista de possíveis estados futuros com base na deliberação.
        """
        objectivos = self.gerar_objectivos()
        return self.seleccionar_objectivos(objectivos)
    
    def gerar_objectivos(self):
        """
        Gera os objetivos com base no estado atual do mundo.

        Retorno:
            Uma lista de objetivos a serem alcançados.
        """
        return [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
    
    def seleccionar_objectivos(self, objectivos):
        """
        Seleciona os objetivos a serem perseguidos com base nos objetivos gerados.

        Argumentos:
            objectivos: Uma lista de objetivos a serem considerados para seleção.

        Retorno:
            Uma lista de objetivos ordenados para perseguição.
        """
        return objectivos.sort(key=self.__modelo_mundo.distancia)
