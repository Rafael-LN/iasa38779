package agente;

import ambiente.Comando;

public class Accao {

    private Comando comando;
    
    public Accao(Comando comando){
        this.comando = comando;
    }

    public Comando getComando() {
        return comando;
    }
}
