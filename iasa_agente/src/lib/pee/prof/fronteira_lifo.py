from pee.mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):
    """
    A classe FronteiraLIFO implementa uma fronteira para a procura em espaço de estados utilizando uma política de Last-In-First-Out (LIFO).

    Esta estrutura de dados é usada para armazenar e recuperar nós durante o processo de procura, garantindo que o nó mais recentemente inserido é o primeiro a ser retirado.

    Herda:
        Fronteira: Classe base que define a interface para diferentes tipos de fronteiras.

    Métodos:
        inserir(self, no): Insere um nó na fronteira utilizando a política LIFO.
    """

    def inserir(self, no):
        """
        Insere um nó na fronteira utilizando a política LIFO.

        Parâmetros:
            no: O nó a ser inserido na fronteira.

        Este método adiciona o nó ao final da lista interna de nós (_nos), garantindo que será o primeiro a ser retirado quando necessário.
        """
        self._nos.append(no)
