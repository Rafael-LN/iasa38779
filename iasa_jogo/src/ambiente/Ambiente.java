package ambiente;

public interface Ambiente {

    public void evoluir();

    /**
     * O Ambiente ao observar gera um certo Evento
     * @return Evento 
     */
    public Evento observar();

    /**
     * O Ambiente irá executar um Comando
     * @param comando
     */
    public void executar(Comando comando);
}