package maqest;

import java.util.HashMap;
import java.util.Map;

import agente.Accao;
import ambiente.Evento;

/**
 * Classe que representa um estado de uma máquina de estados.
 * Cada estado possui um nome e pode ter transições associadas a eventos específicos.
 */
public class Estado {

    public String nome;
    private Map<Evento, Transicao> transicoes;

    /**
     * Construtor para criar um novo estado com o nome especificado.
     * Inicializa o mapa de transições.
     */
    public Estado(String nome) {
        this.nome = nome;
        transicoes = new HashMap<Evento, Transicao>();
    }

    /**
     * Processa um evento para determinar a transição associada.
     */
    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    /**
     * Define uma transição de estado associada a um evento, sem ação associada.
     * @param evento O evento que desencadeia a transição.
     * @param estadoSucessor O estado sucessor após a transição.
     * @return O estado atual.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor) {
        return transicao(evento, estadoSucessor, null);
    }

    /**
     * Define uma transição de estado associada a um evento e uma ação.
     * @param evento O evento que desencadeia a transição.
     * @param estadoSucessor O estado sucessor após a transição.
     * @param accao A ação a ser realizada durante a transição.
     * @return O estado atual.
     */
    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {
        Transicao transicao = new Transicao(estadoSucessor, accao);
        transicoes.put(evento, transicao);
        return this;
    }
    
}
