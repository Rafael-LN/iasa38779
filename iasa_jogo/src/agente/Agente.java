package agente;

import ambiente.Ambiente;

public class Agente {
    
    /**
     * Um Agente é caracterizado por um dado ambiente e um Controlo
     * @param ambiente
     * @param controlo
     */
    public Agente(Ambiente ambiente, Controlo controlo){}

    public void executar(){}

    Percepcao percepcionar(){
        return new Percepcao(null);
    }

    void actuar(Accao accao){}

}
