from abc import ABC, abstractmethod

class ModeloPlan(ABC):
    """
    Classe abstrata que define a interface para um modelo de planeamento.
    Este modelo é utilizado pelo planeador para obter o estado inicial, os estados válidos e os operadores disponíveis no domínio do problema.
    """

    @abstractmethod
    def obter_estado(self):
        """
        Método abstrato para obter o estado inicial do modelo de planeamento.

        Retorna:
        O estado inicial do modelo de planeamento.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer o estado inicial a partir do qual o planeamento começará.
        É essencial para definir o ponto de partida no espaço de estados.
        """
        pass

    @abstractmethod
    def obter_estados(self):
        """
        Método abstrato para obter todos os estados válidos do modelo de planeamento.

        Retorna:
        Uma lista de estados válidos no modelo de planeamento.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer todos os estados possíveis no domínio do problema.
        É necessário para processos que necessitam conhecer todos os estados válidos, como processos de decisão de Markov.
        """
        pass

    @abstractmethod
    def obter_operadores(self):
        """
        Método abstrato para obter os operadores disponíveis no modelo de planeamento.

        Retorna:
        Uma lista de operadores que podem ser aplicados aos estados no modelo de planeamento.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer os operadores (ações) que podem transformar um estado em outro.
        É crucial para definir as transições possíveis no espaço de estados.
        """
        pass
