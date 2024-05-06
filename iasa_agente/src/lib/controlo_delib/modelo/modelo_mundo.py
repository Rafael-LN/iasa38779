from math import dist
from mod.operador import Operador
from sae.ambiente.elemento import Elemento

class ModeloMundo(Operador):
    """
    Classe que representa o modelo do mundo.

    Atributos:
        __operadores (list): Lista de operadores disponíveis.
        __estado (objeto): Estado atual do modelo do mundo.
        __estados (list): Lista de estados conhecidos.
        __elementos (dict): Mapeamento de posição para elementos do ambiente.
        __alterado (bool): Indica se o modelo do mundo foi alterado.

    Métodos:
        __init__: Inicializa o modelo do mundo.
        elementos: Obtém os elementos do ambiente mapeados por posição.
        alterado: Verifica se o modelo do mundo foi alterado.
        obter_estado: Obtém o estado atual do modelo do mundo.
        obter_estados: Obtém a lista de estados conhecidos do modelo do mundo.
        obter_operadores: Obtém a lista de operadores disponíveis para o modelo do mundo.
        obter_elemento: Obtém o elemento do ambiente na posição especificada pelo estado.
        distancia: Calcula a distância do estado especificado ao estado atual do modelo do mundo.
        actualizar: Atualiza o modelo do mundo com base na percepção recebida.
        mostrar: Mostra o modelo do mundo na vista especificada.
    """

    def __init__(self):
        """
        Inicializa o modelo do mundo.
        """
        self.__operadores = []  # Lista de operadores disponíveis
        self.__estado = 0  # Estado atual do modelo do mundo
        self.__estados = []  # Lista de estados conhecidos
        self.__elementos = {}  # Mapeamento de posição para elementos do ambiente
        self.__alterado = False  # Indica se o modelo do mundo foi alterado

    @property
    def elementos(self):
        """
        Obtém os elementos do ambiente mapeados por posição.

        Retorno:
            Um dicionário que mapeia posições para elementos do ambiente.
        """
        return self.__elementos
    
    @property
    def alterado(self):
        """
        Verifica se o modelo do mundo foi alterado.

        Retorno:
            True se o modelo do mundo foi alterado, False caso contrário.
        """
        return self.__alterado
    
    def obter_estado(self):
        """
        Obtém o estado atual do modelo do mundo.

        Retorno:
            O estado atual do modelo do mundo.
        """
        return self.__estado
    
    def obter_estados(self):
        """
        Obtém a lista de estados conhecidos do modelo do mundo.

        Retorno:
            Uma lista de estados conhecidos do modelo do mundo.
        """
        return self.__estados
    
    def obter_operadores(self):
        """
        Obtém a lista de operadores disponíveis para o modelo do mundo.

        Retorno:
            Uma lista de operadores disponíveis para o modelo do mundo.
        """
        return self.__operadores
    
    def obter_elemento(self, estado):
        """
        Obtém o elemento do ambiente na posição especificada pelo estado.

        Argumentos:
            estado: O estado que contém a posição do elemento a ser obtido.

        Retorno:
            O elemento do ambiente na posição especificada pelo estado.
        """
        if estado in self.__elementos:
            return self.__elementos[estado]
        else:
            return None
    
    def distancia(self, estado):
        """
        Calcula a distância do estado especificado ao estado atual do modelo do mundo.

        Argumentos:
            estado: O estado para o qual calcular a distância.

        Retorno:
            A distância entre o estado especificado e o estado atual do modelo do mundo.
        """
        # Verifica se o estado especificado está presente nos estados do modelo do mundo
        if estado in self.__estados:
            # Calcula a distância entre os estados usando dist
            return dist(estado, self.__estado)
        else:
            # Se o estado especificado não estiver presente no modelo do mundo, retorna None
            return None
    
    def actualizar(self, percepcao):
        """
        Atualiza o modelo do mundo com base na percepção recebida.

        Argumentos:
            percepcao: A percepção recebida do ambiente.
        """
        self.__estado = percepcao.estado_agente

        for posicao, elemento in percepcao.elementos.items():
            self.__elementos[posicao] = elemento

        self.alterado = True

    def mostrar(self, vista):
        """
        Mostra o modelo do mundo na vista especificada.

        Argumentos:
            vista: A vista na qual mostrar o modelo do mundo.
        """
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)
