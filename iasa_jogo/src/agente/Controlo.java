package agente;

/**
 * A interface Controlo define  
 */
public interface Controlo {

    /**
     * Ao processar uma precepcao é gerado uma accao com base nessa percepcao
     * @param percepcao
     * @return Accao
     */
    public Accao processar(Percepcao percepcao);
}
