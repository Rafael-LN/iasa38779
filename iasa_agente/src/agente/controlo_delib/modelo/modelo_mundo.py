from math import dist
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento

class ModeloMundo(ModeloPlan):
    """
    Classe que implementa o modelo do mundo para um agente autónomo.
    Herda da classe ModeloPlan e fornece informações sobre o estado atual do mundo, os operadores disponíveis e os elementos presentes no ambiente.
    """

    def __init__(self):
        """
        Inicializa uma nova instância de ModeloMundo.

        Funcionalidade:
        Este construtor inicializa os operadores disponíveis, o estado atual do modelo do mundo, a lista de estados conhecidos,
        um dicionário de elementos do ambiente e um indicador de alterações no modelo do mundo.
        """
        self.__operadores = [OperadorMover(self, direcao) for direcao in Direccao]  # Lista de operadores disponíveis
        self.__estado = None  # Estado atual do modelo do mundo
        self.__estados = []  # Lista de estados conhecidos
        self.__elementos = dict()  # Mapeamento de posição para elementos do ambiente
        self.__alterado = False  # Indica se o modelo do mundo foi alterado

    @property
    def elementos(self):
        """
        Retorna o dicionário de elementos do ambiente.

        Retorna:
        Um dicionário que mapeia posições para elementos do ambiente.
        """
        return self.__elementos

    @property
    def alterado(self):
        """
        Indica se o modelo do mundo foi alterado.

        Retorna:
        True se o modelo do mundo foi alterado, False caso contrário.
        """
        return self.__alterado

    def obter_estado(self):
        """
        Obtém o estado atual do modelo do mundo.

        Retorna:
        O estado atual do modelo do mundo.
        """
        return self.__estado

    def obter_estados(self):
        """
        Obtém a lista de estados conhecidos do modelo do mundo.

        Retorna:
        Uma lista de estados conhecidos.
        """
        return self.__estados

    def obter_operadores(self):
        """
        Obtém a lista de operadores disponíveis no modelo do mundo.

        Retorna:
        Uma lista de operadores que podem ser aplicados no modelo do mundo.
        """
        return self.__operadores

    def obter_elemento(self, estado):
        """
        Obtém o elemento presente numa determinada posição do estado.

        Parâmetros:
        estado: O estado cuja posição será utilizada para obter o elemento correspondente.

        Retorna:
        O elemento presente na posição do estado fornecido, ou None se não houver elemento na posição.
        """
        return self.__elementos.get(estado)

    def distancia(self, estado):
        """
        Calcula a distância entre o estado atual e um estado fornecido.

        Parâmetros:
        estado: O estado para o qual se pretende calcular a distância.

        Retorna:
        A distância euclidiana entre o estado atual e o estado fornecido.
        """
        return dist(self.__estado.posicao, estado.posicao)

    def actualizar(self, percepcao):
        """
        Atualiza o modelo do mundo com base numa nova perceção do ambiente.

        Parâmetros:
        percepcao: A perceção recebida do ambiente.

        Funcionalidade:
        Este método atualiza o estado atual do agente com base na perceção e verifica se houve mudanças nos elementos do ambiente.
        Se houver mudanças, atualiza a lista de estados conhecidos e marca o modelo do mundo como alterado.
        """
        self.__estado = EstadoAgente(percepcao.posicao)

        if self.__elementos != percepcao.elementos:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percepcao.posicoes]
            self.__alterado = True
        else:
            self.__alterado = False

    def mostrar(self, vista):
        """
        Mostra a visualização do modelo do mundo utilizando uma vista fornecida.

        Parâmetros:
        vista: Objeto responsável por exibir a visualização do modelo do mundo.

        Funcionalidade:
        Este método percorre os elementos do ambiente e utiliza a vista para mostrar elementos relevantes como alvos e obstáculos.
        Adicionalmente, marca a posição do estado atual do agente na vista.
        """
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)
