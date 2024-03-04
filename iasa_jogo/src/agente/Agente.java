package agente;

import ambiente.Ambiente;

public class Agente {

    private Ambiente ambiente;
    private Controlo controlo;
    /**
     * Um Agente está inserido num ambiente e tem um controlo especifico
     * @param ambiente
     * @param controlo
     */
    public Agente(Ambiente ambiente, Controlo controlo){
        this.ambiente = ambiente;
        this.controlo = controlo;
    }

    /**
     * O Agente actua através de uma accao que adquire
     * através do processamento de uma precepção que obtém de observar o ambiente
     */
    public void executar(){
        Percepcao percepcao = percepcionar();
        Accao accao = controlo.processar(percepcao);
        actuar(accao);
    }

    /**
     * O Agente observa o ambiente para gerar uma percepcao
     */
    protected Percepcao percepcionar(){
        return new Percepcao(ambiente.observar());
    }

    // O Agente executa um comando no ambiente através de uma accao
    protected void actuar(Accao accao){
        if (accao != null) {
            ambiente.executar(accao.getComando());            
        }
    }

}
