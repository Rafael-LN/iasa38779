package maqest;

import agente.Accao;

/**
 * Classe que representa uma transição de estado de uma máquina de estados.
 * Esta classe associa um estado sucessor a uma ação que deve ser realizada durante a transição.
 */
public class Transicao {

    private Estado estadoSuccessor;
    private Accao acao;
    
    /**
     * Construtor para criar uma nova transição com o estado sucessor e a ação especificados.
     */
    public Transicao(Estado estadoSuccessor, Accao accao) {
        this.estadoSuccessor = estadoSuccessor;
        this.acao = accao;
    }

  /**
     * Obtém o estado sucessor associado à transição.
     * @return O estado sucessor após a transição.
     */
    public Estado getEstadoSuccessor() {
        return estadoSuccessor;
    }

    /**
     * Obtém a ação associada à transição.
     * @return A ação a ser realizada durante a transição.
     */
    public Accao getAcao() {
        return acao;
    }
}
