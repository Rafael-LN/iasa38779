package agente;

import ambiente.Evento;

/**
 * Classe que representa uma percepção obtida do ambiente.
 * Uma percepção tem um evento associado.
 */
public class Percepcao {

    private Evento evento;

    /**
     * Construtor para criar uma nova percepção com o evento especificado.
     */
    public Percepcao(Evento evento){
        this.evento = evento;
    }

    /**
     * Obtém o evento associado a esta percepção.
     */
    public Evento getEvento() {
        return evento;
    }
}

