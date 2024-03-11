package maqest;

import agente.Accao;

public class Transicao {

    private Estado estadoSuccessor;
    private Accao acao;
    
    public Transicao(Estado estadoSuccessor, Accao accao) {
        this.estadoSuccessor = estadoSuccessor;
        this.acao = accao;
    }

    public Estado getEstadoSuccessor() {
        return estadoSuccessor;
    }

    public Accao getAcao() {
        return acao;
    }
}
