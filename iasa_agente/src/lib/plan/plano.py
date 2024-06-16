from abc import ABC, abstractmethod

class Plano(ABC):
    """
    Classe abstrata que define a interface para um plano de ações no contexto de um agente autónomo.
    Esta classe serve como base para a implementação de diferentes tipos de planos que podem ser gerados por vários mecanismos de planeamento.
    """

    @abstractmethod
    def obter_accao(self, estado):
        """
        Método abstrato para obter a ação correspondente a um determinado estado.

        Parâmetros:
        estado: O estado para o qual se pretende obter a ação correspondente.

        Retorna:
        A ação associada ao estado fornecido. O tipo de retorno específico será definido nas subclasses concretas.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer a ação adequada baseada no estado fornecido.
        É um ponto de extensão para diferentes tipos de planos que podem ter mecanismos variados para determinar ações com base em estados.
        """
        pass

    @abstractmethod
    def mostrar(self, vista):
        """
        Método abstrato para exibir a sequência de ações do plano utilizando uma vista fornecida.

        Parâmetros:
        vista: Objeto responsável por exibir a visualização das ações do plano.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para fornecer uma maneira de visualizar o plano.
        A implementação específica dependerá de como a informação do plano deve ser exibida, e do formato de visualização suportado pela vista fornecida.
        """
        pass
