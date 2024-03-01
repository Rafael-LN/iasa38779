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

    public void executar(){
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
        ambiente.evoluir();
    }

    protected Percepcao percepcionar(){
        return new Percepcao(ambiente.observar());
    }

    protected void actuar(Accao accao){
        ambiente.executar(accao.getComando());
    }

}
