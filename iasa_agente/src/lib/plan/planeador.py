from abc import ABC, abstractmethod

class Planeador(ABC):
    """
    Classe abstrata que define a interface para um planeador em algoritmos de procura.
    Um planeador é responsável por gerar um plano de ações que permita alcançar os objetivos a partir de um modelo de planeamento.
    """

    @abstractmethod
    def planear(self, modelo_plan, objectivos):
        """
        Gera um plano de ações para alcançar os objetivos a partir do modelo de planeamento.

        Parâmetros:
        modelo_plan: O modelo de planeamento que define os estados e operadores.
        objectivos: A lista de objetivos que se pretende alcançar.

        Retorna:
        Um plano de ações que permite alcançar os objetivos.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer a lógica de geração de planos de ações.
        A implementação deve utilizar o modelo de planeamento e os objetivos para determinar a sequência de ações necessária para atingir os objetivos.
        """
        pass
