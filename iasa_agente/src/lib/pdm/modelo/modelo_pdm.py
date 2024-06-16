from abc import ABC, abstractmethod

class ModeloPDM(ABC):
    """
    Classe abstrata que define a interface para um modelo de Processos de Decisão Markovianos (PDM).
    Um PDM é caracterizado por um conjunto de estados, um conjunto de ações, uma função de transição, uma função de recompensa e uma função de sucessores.
    """

    @abstractmethod
    def S(self):
        """
        Retorna o conjunto de estados possíveis no PDM.

        Retorna:
        Um iterador ou uma coleção de estados possíveis.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer todos os estados possíveis no PDM.
        """
        pass

    @abstractmethod
    def A(self, s):
        """
        Retorna o conjunto de ações possíveis a partir de um estado dado.

        Parâmetros:
        s: O estado atual.

        Retorna:
        Um iterador ou uma coleção de ações possíveis a partir do estado s.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer todas as ações possíveis a partir de um estado específico.
        """
        pass

    @abstractmethod
    def T(self, s, a):
        """
        Retorna a função de transição que define a probabilidade de transitar de um estado para outro dado uma ação.

        Parâmetros:
        s: O estado atual.
        a: A ação a ser aplicada.

        Retorna:
        Um dicionário ou uma coleção onde as chaves são estados sucessores e os valores são as probabilidades de transição.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer a função de transição do PDM.
        """
        pass

    @abstractmethod
    def R(self, s, a, sn):
        """
        Retorna a função de recompensa que define a recompensa recebida ao transitar de um estado para outro dado uma ação.

        Parâmetros:
        s: O estado atual.
        a: A ação aplicada.
        sn: O estado sucessor.

        Retorna:
        A recompensa associada à transição do estado s para o estado sn através da ação a.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer a função de recompensa do PDM.
        """
        pass

    @abstractmethod
    def suc(self, s, a):
        """
        Retorna os estados sucessores possíveis ao aplicar uma ação em um estado.

        Parâmetros:
        s: O estado atual.
        a: A ação aplicada.

        Retorna:
        Um iterador ou uma coleção de estados sucessores possíveis.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer os estados sucessores possíveis no PDM ao aplicar uma ação em um estado.
        """
        pass
