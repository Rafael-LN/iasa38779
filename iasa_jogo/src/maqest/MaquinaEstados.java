package maqest;

import agente.Accao;
import ambiente.Evento;

public class MaquinaEstados {

    private Estado estado;
    
    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    public Estado getEstado() {
        return estado;
    }

    public Accao processar(Evento evento) {
        Transicao transicao = estado.processar(evento);
        if(transicao != null) {
            estado = transicao.getEstadoSuccessor();
            return transicao.getAcao();
        }
        return null;
    }
}
