package agente;

import ambiente.Comando;
/**
 * Classe que representa uma acção a ser realizada.
 * Uma accao tem um comando associado.
 */
public class Accao {

    private Comando comando;

    /**
     * Construtor para criar uma nova acção com o comando especificado.
     */
    public Accao(Comando comando){
        this.comando = comando;
    }

    /**
     * Obtém o comando associado a esta ação.
     */
    public Comando getComando() {
        return comando;
    }
}
