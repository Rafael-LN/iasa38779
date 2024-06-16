from math import cos, dist, sin
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from sae.agente.accao import Accao

class OperadorMover:
    """
    Classe que implementa o operador de movimento para um agente.
    Permite mover o agente numa direção específica, alterando a sua posição no modelo do mundo.
    """

    def __init__(self, modelo_mundo, direccao):
        """
        Inicializa uma nova instância de OperadorMover.

        Parâmetros:
        modelo_mundo: O modelo do mundo que contém os estados e elementos.
        direccao: A direção na qual o agente se moverá.

        Funcionalidade:
        Este construtor inicializa o modelo do mundo, o ângulo da direção e a ação correspondente ao operador de movimento.
        """
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Accao(direccao)

    @property
    def ang(self):
        """
        Obtém o ângulo da direção de movimento.

        Retorna:
        O ângulo da direção de movimento.

        Funcionalidade:
        Este método retorna o valor do ângulo da direção de movimento.
        """
        return self.__ang

    @property
    def accao(self):
        """
        Obtém a ação correspondente ao operador de movimento.

        Retorna:
        A ação correspondente ao operador de movimento.

        Funcionalidade:
        Este método retorna a instância da ação correspondente ao operador de movimento.
        """
        return self.__accao

    def aplicar(self, estado):
        """
        Aplica o operador de movimento ao estado atual, gerando um novo estado.

        Parâmetros:
        estado: O estado atual do agente.

        Retorna:
        O novo estado do agente após a aplicação do operador de movimento, ou None se o estado não for válido.

        Funcionalidade:
        Este método calcula a nova posição do agente aplicando a translação e verifica se o novo estado é válido.
        Se for válido, retorna o novo estado; caso contrário, retorna None.
        """
        # Fazer a translação para obter a nova posição
        nova_posicao = self.__translacao(estado.posicao, self.accao.passo, self.ang)

        # Criar um estado agente para a nova posição
        novo_estado = EstadoAgente(nova_posicao)

        # Validar se o estado é válido:
        if novo_estado in self.__modelo_mundo.obter_estados():
            # Se esse estado for um estado do modelo do mundo, então retorna esse estado
            return novo_estado

    def custo(self, estado, estado_suc):
        """
        Calcula o custo de aplicar o operador de movimento entre dois estados.

        Parâmetros:
        estado: O estado atual do agente.
        estado_suc: O estado sucessor após a aplicação do operador de movimento.

        Retorna:
        O custo de transição entre o estado atual e o estado sucessor.

        Funcionalidade:
        Este método calcula o custo de transição como a distância euclidiana entre as posições dos estados,
        com um valor mínimo de 1. Se o estado sucessor for None, retorna None.
        """
        if estado_suc:
            return max(1, dist(estado_suc.posicao, estado.posicao))

    def __translacao(self, posicao, distancia, angulo):
        """
        Calcula a nova posição do agente após a aplicação do operador de movimento.

        Parâmetros:
        posicao: A posição atual do agente.
        distancia: A distância a ser percorrida pelo agente.
        angulo: O ângulo da direção de movimento.

        Retorna:
        A nova posição do agente após a translação.

        Funcionalidade:
        Este método calcula as novas coordenadas do agente aplicando a translação baseada na distância e ângulo fornecidos.
        """
        x, y = posicao  # Extrai as coordenadas x e y da posição inicial

        # Calcula as novas coordenadas após a translação
        dx = round(distancia * cos(angulo))
        dy = -round(distancia * sin(angulo))
        
        return (x + dx, y + dy)
