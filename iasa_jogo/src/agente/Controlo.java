package agente;

/**
 * Interface que define o comportamento para o controlo de um sistema,
 * onde uma percepção é processada para gerar uma acção correspondente.
 */
public interface Controlo {

    /**
     * Processa uma percepção e gera uma acção correspondente.
     */
    public Accao processar(Percepcao percepcao);
}
