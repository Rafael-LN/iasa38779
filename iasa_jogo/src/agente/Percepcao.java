package agente;

import ambiente.Evento;

public class Percepcao {

    private Evento evento;

    /**
     * A percepcao é caracterizada por um Evento
     * @param evento
     */
    public Percepcao(Evento evento){
        this.evento = evento;
    }

    public Evento getEvento() {
        return evento;
    }
}
