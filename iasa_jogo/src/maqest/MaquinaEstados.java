package maqest;

import agente.Accao;
import ambiente.Evento;

/**
 * Classe que implementa uma máquina de estados para controlar o comportamento de um sistema.
 * Esta classe mantém o estado atual e processa eventos para determinar transições de estado e ações associadas.
 */
public class MaquinaEstados {

    private Estado estado;
    
    /**
     * Construtor para criar uma nova máquina de estados com o estado inicial especificado.
     * @param estadoInicial O estado inicial da máquina de estados.
     */
    public MaquinaEstados(Estado estadoInicial) {
        this.estado = estadoInicial;
    }

    /**
     * Obtém o estado atual da máquina de estados.
     */
    public Estado getEstado() {
        return estado;
    }

    /**
     * Processa um evento na máquina de estados para determinar uma transição de estado e a ação associada.
     * @param evento O evento a ser processado.
     * @return A ação associada à transição de estado, ou null se não houver transição.
     */
    public Accao processar(Evento evento) {
        Transicao transicao = estado.processar(evento);
        
        if (transicao != null) {
            estado = transicao.getEstadoSuccessor();
            return transicao.getAcao();
        }
        return null;
    }
}
