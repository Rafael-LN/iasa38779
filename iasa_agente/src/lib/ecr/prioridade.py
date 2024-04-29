from ecr.comport_comp import ComportComp


class Prioridade(ComportComp):
    """
    Classe que representa um comportamento composto com prioridade, derivada da classe ComportComp.
    """

    def seleccionar_accao(self, accoes):
        """
        Seleciona a ação com maior prioridade entre as ações fornecidas.

        :param accoes: Lista de ações para seleção.
        :return: Ação com a maior prioridade.
        """
        maior = accoes[0]
        for accao in accoes:
            if accao.prioridade > maior.prioridade:
                maior = accao
        return maior
