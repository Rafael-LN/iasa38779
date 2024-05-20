from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    """
    A interface ModeloPDM define a estrutura para a modelação de Processos de Decisão de Markov (PDM).
    
    Um Processo de Decisão de Markov é utilizado para modelar a tomada de decisão sequencial
    onde os resultados são parcialmente aleatórios e parcialmente sob o controlo de um agente decisor.
    
    Esta interface inclui métodos abstratos para:
    - Definir o conjunto de estados (S).
    - Definir o conjunto de ações possíveis (A) em cada estado.
    - Modelar a transição de estados (T), que define a probabilidade de transição entre estados após uma ação.
    - Modelar a recompensa (R) associada a uma transição de estado.
    - Determinar os estados sucessores (suc) possíveis após a execução de uma ação.
    """

    @abstractmethod
    def S(self):
        """
        Retorna o conjunto de estados possíveis (S) do mundo.
        
        :return: Conjunto de estados possíveis.
        """
        pass

    @abstractmethod
    def A(self, s):
        """
        Retorna o conjunto de ações possíveis (A) num estado específico (s).
        
        :param s: Estado atual.
        :return: Conjunto de ações possíveis no estado s.
        """
        pass

    @abstractmethod
    def T(self, s, a, sn):
        """
        Define o modelo de transição de estados (T), ou seja, a probabilidade de transição do estado s para o estado sn através da ação a.
        
        :param s: Estado atual.
        :param a: Ação realizada.
        :param sn: Estado subsequente.
        :return: Probabilidade de transição de s para sn através de a.
        """
        pass

    @abstractmethod
    def R(self, s, a, sn):
        """
        Define o modelo de recompensa (R), que representa o ganho ou perda esperado na transição de s para sn através de a.
        
        :param s: Estado atual.
        :param a: Ação realizada.
        :param sn: Estado subsequente.
        :return: Recompensa esperada na transição de s para sn através de a.
        """
        pass

    @abstractmethod
    def suc(self, s, a):
        """
        Retorna os estados sucessores possíveis (s') ao aplicar a ação a no estado s.
        
        :param s: Estado atual.
        :param a: Ação realizada.
        :return: Conjunto de estados sucessores possíveis após aplicar a ação a em s.
        """
        pass
