from abc import ABC, abstractmethod

class Operador(ABC):
    """
    Classe abstrata que define a interface para operadores utilizados em algoritmos de procura.
    Um operador é responsável por transformar um estado em um estado sucessor e calcular o custo dessa transformação.
    """

    @abstractmethod
    def aplicar(self, estado):
        """
        Aplica o operador a um estado, gerando um estado sucessor.

        Parâmetros:
        estado: O estado atual ao qual o operador será aplicado.

        Retorna:
        O estado sucessor resultante da aplicação do operador.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para definir a lógica de transformação do estado atual em um estado sucessor.
        """
        pass

    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Calcula o custo de aplicar o operador para transformar um estado em um estado sucessor.

        Parâmetros:
        estado: O estado atual.
        estado_suc: O estado sucessor resultante da aplicação do operador.

        Retorna:
        O custo de transformar o estado atual no estado sucessor.

        Funcionalidade:
        Este método deve ser implementado pelas subclasses para definir a lógica de cálculo do custo da transformação de um estado em outro.
        O custo é utilizado pelos algoritmos de procura para avaliar a viabilidade e eficiência dos caminhos explorados.
        """
        pass
