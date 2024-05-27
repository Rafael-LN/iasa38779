from lib.plan.modelo.modelo_plan import ModeloPlan
from pdm.modelo.modelo_pdm import ModeloPDM


class ModeloPDMPlan(ModeloPDM, ModeloPlan):
    """
    A classe ModeloPDMPlan combina funcionalidades de ModeloPDM e ModeloPlan para realizar planeamento baseado em Processos de Decisão de Markov (PDM).

    Atributos:
        modelo_plan (ModeloPlan): Uma instância de ModeloPlan que define o modelo de planeamento.
        objectivos (list): Lista de estados objetivo.
        rmax (int): Recompensa máxima atribuída ao alcançar um objetivo.
        __transicoes (dict): Dicionário que armazena transições de estados para facilitar o cálculo das funções de transição.

    Métodos:
        __init__(self, modelo_plan, objectivos, rmax=1000): Inicializa a instância da classe com os parâmetros fornecidos.
        obter_estado(self): Retorna o estado atual do modelo de planeamento.
        obter_estados(self): Retorna todos os estados válidos no modelo de planeamento.
        obter_operadores(self): Retorna todos os operadores válidos no modelo de planeamento.
        S(self): Retorna o conjunto de todos os estados válidos.
        A(self, s): Retorna o conjunto de operadores válidos para um estado, ou uma lista vazia se o estado é um objetivo.
        T(self, s, a): Calcula a probabilidade de transição de um estado para outro dado um operador.
        R(self, s, a, sn): Calcula a recompensa para uma transição de estado dada por um operador.
        suc(self, s, a): Retorna o estado sucessor resultante da aplicação de um operador a um estado.
    """

    def __init__(self, modelo_plan, objectivos, rmax=1000):
        """
        Inicializa uma instância da classe ModeloPDMPlan.

        Parâmetros:
            modelo_plan (ModeloPlan): Instância de ModeloPlan que define o modelo de planeamento.
            objectivos (list): Lista de estados objetivo.
            rmax (int, opcional): Recompensa máxima para alcançar um objetivo, com valor padrão de 1000.

        Este método também inicializa o dicionário de transições, calculando os estados sucessores para cada par (estado, operador).
        """
        self.__modelo_plan = modelo_plan 
        self.__objectivos = objectivos
        self.rmax = rmax

        self.__transicoes = {}
        for s in self.obter_estados():
            for a in self.obter_operadores():
                if sn := a.aplicar(s):
                    self.__transicoes[(s, a)] = sn


    def obter_estado(self):
        """
        Retorna o estado atual do modelo de planeamento.

        Retorna:
            Estado atual do modelo de planeamento.
        """
        return self.__modelo_plan.obter_estado()

    def obter_estados(self):
        """
        Retorna o conjunto de todos os estados válidos no modelo de planeamento.

        Retorna:
            list: Lista de estados válidos.
        """
        return self.__modelo_plan.obter_estados()

    
    def obter_operadores(self):
        """
        Retorna o conjunto de todos os operadores válidos no modelo de planeamento.

        Retorna:
            list: Lista de operadores válidos.
        """
        return self.__modelo_plan.obter_operadores()

    def S(self):
        """
        Retorna o conjunto de todos os estados válidos.

        Este método é uma conveniência para compatibilidade com a notação usual de PDM.

        Retorna:
            list: Lista de estados válidos.
        """
        return self.obter_estados()

    
    def A(self, s):
        """
        Retorna o conjunto de operadores válidos para um estado dado.

        Se o estado é um dos objetivos, retorna uma lista vazia, indicando que não há mais ações a serem tomadas.

        Parâmetros:
            s: Estado para o qual se deseja obter os operadores.

        Retorna:
            list: Lista de operadores válidos ou lista vazia se o estado é um objetivo.
        """
        return self.obter_operadores() if s not in self.__objectivos else []

    
    def T(self, s, a):
        """
        Calcula a probabilidade de transição de um estado s para um estado sucessor dado um operador a.

        Parâmetros:
            s: Estado atual.
            a: Operador a ser aplicado.

        Retorna:
            int: 1 se a transição é possível, caso contrário 0.
        """
        sn = self.__transicoes.get((s, a))
        return 1 if sn is not None else 0

    
    def R(self, s, a, sn):
        """
        Calcula a recompensa associada a uma transição de estado s para um estado sucessor sn dado um operador a.

        A recompensa é negativa pelo custo da ação e positiva se o estado sucessor é um dos objetivos, adicionando rmax.

        Parâmetros:
            s: Estado atual.
            a: Operador aplicado.
            sn: Estado sucessor.

        Retorna:
            int: Valor da recompensa calculada.
        """
        recompensa = -a.custo(s, sn)

        if sn in self.__objectivos:
            recompensa += self.rmax

        return recompensa

    
    def suc(self, s, a):
        """
        Retorna o estado sucessor resultante da aplicação de um operador a um estado s.

        Parâmetros:
            s: Estado atual.
            a: Operador aplicado.

        Retorna:
            list: Lista contendo o estado sucessor ou lista vazia se não há sucessor.
        """
        sn = self.__transicoes.get((s, a))
        return [sn] if sn else []

