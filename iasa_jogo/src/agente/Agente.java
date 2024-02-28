package agente;

import ambiente.Ambiente;

public class Agente {

    private Ambiente ambiente;
    private Controlo controlo;
    /**
     * Um Agente é caracterizado por um dado ambiente e um Controlo
     * @param ambiente
     * @param controlo
     */
    public Agente(Ambiente ambiente, Controlo controlo){
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    public void executar(){}

    protected Percepcao percepcionar(){
        return new Percepcao(null);
    }

    protected void actuar(Accao accao){}

}
