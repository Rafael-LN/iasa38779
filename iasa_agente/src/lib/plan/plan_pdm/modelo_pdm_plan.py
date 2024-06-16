from lib.plan.modelo.modelo_plan import ModeloPlan
from pdm.modelo.modelo_pdm import ModeloPDM

class ModeloPDMPlan(ModeloPDM, ModeloPlan):
    """
    Classe que combina as funcionalidades de um modelo de planeamento (ModeloPlan) e de um processo de decisão Markoviano (ModeloPDM).
    Esta classe é utilizada para suportar o planeamento automático com base em PDM.
    """

    def __init__(self, modelo_plan, objectivos, rmax=1000):
        """
        Inicializa uma nova instância de ModeloPDMPlan.

        Parâmetros:
        modelo_plan: O modelo de planeamento que define os estados e operadores.
        objectivos: A lista de estados objetivo que se pretende alcançar.
        rmax: A recompensa máxima atribuída ao alcançar um objetivo.

        Funcionalidade:
        Este construtor inicializa o modelo de planeamento, os objetivos e a recompensa máxima. Também cria um dicionário de transições para armazenar os estados sucessores resultantes da aplicação dos operadores.
        """
        self.__modelo_plan = modelo_plan
        self.__objectivos = objectivos
        self.__rmax = rmax
        self.__transicoes = {}
        if self.obter_estados() and self.obter_operadores(): 
            for s in self.obter_estados():
                for a in self.obter_operadores():
                    if sn := a.aplicar(s):
                        self.__transicoes[(s, a)] = sn

    def obter_estado(self):
        """
        Obtém o estado atual do modelo de planeamento.

        Retorna:
        O estado atual do modelo de planeamento.
        """
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        """
        Obtém a lista de estados conhecidos do modelo de planeamento.

        Retorna:
        Uma lista de estados conhecidos.
        """
        return self.__modelo_plan.obter_estados()

    def obter_operadores(self):
        """
        Obtém a lista de operadores disponíveis no modelo de planeamento.

        Retorna:
        Uma lista de operadores que podem ser aplicados no modelo de planeamento.
        """
        return self.__modelo_plan.obter_operadores()

    def S(self):
        """
        Retorna o conjunto de estados possíveis no PDM.

        Retorna:
        Uma lista de estados possíveis.
        """
        return self.obter_estados()

    def A(self, s):
        """
        Retorna o conjunto de ações possíveis a partir de um estado dado.

        Parâmetros:
        s: O estado atual.

        Retorna:
        Uma lista de ações possíveis a partir do estado s, ou uma lista vazia se s for um estado objetivo.
        """
        return self.obter_operadores() if s not in self.__objectivos else []

    def T(self, s, a, sn):
        """
        Retorna a função de transição que define a probabilidade de transitar de um estado para outro dado uma ação.

        Parâmetros:
        s: O estado atual.
        a: A ação a ser aplicada.
        sn: O estado sucessor resultante da aplicação da ação a partir do estado s.

        Retorna:
        1 se sn é o estado sucessor esperado, 0 caso contrário.

        Funcionalidade:
        Este método verifica se a transição de s para sn através de a é válida e retorna a probabilidade de transição correspondente.
        """
        return 1 if sn and (sn == self.__transicoes.get((s, a))) else 0

    def R(self, s, a, sn):
        """
        Retorna a função de recompensa que define a recompensa recebida ao transitar de um estado para outro dado uma ação.

        Parâmetros:
        s: O estado atual.
        a: A ação aplicada.
        sn: O estado sucessor resultante da aplicação da ação a partir do estado s.

        Retorna:
        A recompensa associada à transição do estado s para o estado sn através da ação a.

        Funcionalidade:
        Este método calcula a recompensa da transição, penalizando pelo custo da ação e adicionando uma recompensa extra se o estado sucessor for um objetivo.
        """
        recompensa = -a.custo(s, sn)

        if sn in self.__objectivos:
            recompensa += self.__rmax

        return recompensa

    def suc(self, s, a):
        """
        Retorna os estados sucessores possíveis ao aplicar uma ação em um estado.

        Parâmetros:
        s: O estado atual.
        a: A ação aplicada.

        Retorna:
        Uma lista contendo o estado sucessor se a transição for válida, ou uma lista vazia caso contrário.

        Funcionalidade:
        Este método fornece os estados sucessores possíveis ao aplicar uma ação em um estado, baseado nas transições armazenadas.
        """
        return [self.__transicoes.get((s, a)) for a in self.A(s) if self.__transicoes.get((s, a))]
