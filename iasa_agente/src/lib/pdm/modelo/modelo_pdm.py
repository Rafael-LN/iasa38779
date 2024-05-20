from abc import ABC, abstractmethod
from mod import Estado, Operador

class ModeloPDM(ABC):
    """
    Interface abstrata representante do modelo de Processos de Decisão de Markov (PDM).

    Esta interface define a estrutura para a modelação de um Processo de Decisão de Markov,
    onde a tomada de decisão sequencial é influenciada por resultados parcialmente aleatórios 
    e parcialmente sob o controlo de um agente decisor.

    O PDM é utilizado para representar:
    - O conjunto de estados possíveis do mundo (S).
    - O conjunto de ações que o agente pode executar em cada estado (A).
    - A probabilidade de transição entre estados após a execução de uma ação (T).
    - A recompensa obtida em função da transição entre estados (R).
    - Os estados sucessores possíveis após a execução de uma ação (suc).
    """

    @abstractmethod
    def S(self):
        """
        Método abstrato que representa o conjunto de estados do mundo.

        Num Processo de Decisão de Markov, o conjunto de estados (S) abrange todas as possíveis
        configurações do ambiente onde o agente opera. Estes estados são utilizados para 
        descrever a situação atual do ambiente a cada passo de tempo.

        :return: Conjunto de estados possíveis.
        """
        pass

    @abstractmethod
    def A(self, s):
        """
        Método abstrato que representa o conjunto de ações possíveis num estado específico.

        Em cada estado (s), o agente pode escolher entre um conjunto de ações (A) disponíveis.
        Estas ações representam as possíveis decisões que o agente pode tomar a partir do estado 
        atual, afetando a transição para futuros estados.

        :param s: Estado atual pertencente ao conjunto de estados em S.
        :return: Conjunto de ações possíveis no estado s.
        """
        pass

    @abstractmethod
    def T(self, s, a):
        """
        Método abstrato que representa a probabilidade de transição do estado atual para um estado seguinte através de uma ação.

        A função de transição (T) descreve a dinâmica do ambiente, especificando a probabilidade
        de transição de um estado (s) para um estado sucessor (s') dado que uma ação (a) foi 
        executada. Esta probabilidade reflete a incerteza e a natureza estocástica das transições 
        de estado em ambientes não-determinísticos.

        :param s: Estado atual pertencente ao conjunto de estados em S.
        :param a: Ação a ser aplicada ao estado s.
        :return: Lista de tuplos contendo a probabilidade de transição e o estado seguinte.
        """
        pass

    @abstractmethod
    def R(self, s, a, sn):
        """
        Método abstrato que representa a recompensa esperada pela transição de um estado para outro através de uma ação.

        A função de recompensa (R) quantifica o ganho ou perda esperada ao transitar de um estado 
        (s) para um estado sucessor (sn) através da execução de uma ação (a). Esta recompensa 
        pode ser utilizada para avaliar a qualidade das decisões do agente ao longo do tempo.

        :param s: Estado atual pertencente ao conjunto de estados em S.
        :param a: Ação aplicada ao estado s.
        :param sn: Estado sucessor após a aplicação da ação a no estado s.
        :return: Valor da recompensa (float).
        """
        pass

    @abstractmethod
    def suc(self, s, a):
        """
        Método abstrato que retorna os estados sucessores possíveis após a execução de uma ação num estado.

        A função de sucessores (suc) determina todos os possíveis estados futuros (s') que podem 
        ser alcançados a partir de um estado atual (s) ao aplicar uma ação (a). Este conjunto de 
        estados sucessores é fundamental para prever e planejar as consequências das ações do agente.

        :param s: Estado atual pertencente ao conjunto de estados em S.
        :param a: Ação aplicada ao estado s.
        :return: Conjunto de estados sucessores possíveis.
        """
        pass
