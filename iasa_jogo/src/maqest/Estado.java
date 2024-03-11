package maqest;

import java.util.Map;

import agente.Accao;
import ambiente.Evento;

public class Estado {

    public String nome;
    Map<Evento, Transicao> transicoes;

    public Estado(String nome) {
        this.nome = nome;
    }

    public Transicao processar(Evento evento) {
        return transicoes.get(evento);
    }

    public Estado transicao(Evento evento, Estado estadoSucessor) {}

    public Estado transicao(Evento evento, Estado estadoSucessor, Accao accao) {}
    
}
