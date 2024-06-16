from sae.ambiente.elemento import Elemento

class MecDelib():
    """
    Classe que implementa o mecanismo de deliberação para um agente.
    Este mecanismo é responsável por gerar e selecionar objetivos com base no modelo do mundo do agente.
    """

    def __init__(self, modelo_mundo):
        """
        Inicializa uma nova instância de MecDelib.

        Parâmetros:
        modelo_mundo: O modelo do mundo que representa o estado atual do ambiente do agente.

        Funcionalidade:
        Este construtor inicializa o atributo __modelo_mundo com o modelo do mundo fornecido.
        """
        self.__modelo_mundo = modelo_mundo

    def deliberar(self):
        """
        Realiza o processo de deliberação para determinar os objetivos do agente.

        Retorna:
        Uma lista de objetivos selecionados.

        Funcionalidade:
        Este método gera uma lista de possíveis objetivos através do método gerar_objectivos e,
        em seguida, seleciona os objetivos relevantes utilizando o método seleccionar_objectivos.
        """
        objectivos = self.gerar_objectivos()
        return self.seleccionar_objectivos(objectivos)

    def gerar_objectivos(self):
        """
        Gera uma lista de possíveis objetivos com base no modelo do mundo.

        Retorna:
        Uma lista de estados que são considerados objetivos potenciais.

        Funcionalidade:
        Este método percorre todos os estados válidos no modelo do mundo e seleciona aqueles que contêm o elemento ALVO.
        """
        return [estado for estado in self.__modelo_mundo.obter_estados() if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]

    def seleccionar_objectivos(self, objectivos):
        """
        Seleciona e ordena os objetivos com base na sua distância ao agente.

        Parâmetros:
        objectivos: Uma lista de possíveis objetivos gerados.

        Retorna:
        Uma lista de objetivos ordenados pela distância ao agente, do mais próximo ao mais distante.

        Funcionalidade:
        Este método ordena os objetivos com base na distância ao agente, utilizando a função de distância do modelo do mundo.
        Os objetivos mais próximos são priorizados.
        """
        return sorted(objectivos, key=lambda estado: self.__modelo_mundo.distancia(estado))
