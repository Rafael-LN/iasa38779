package ambiente;

/**
 * Interface que define o comportamento de um ambiente.
 * Um ambiente pode evoluir para um novo estado, gerar eventos ao ser observado
 * e ser executado com base num comando.
 */
public interface Ambiente {

    /**
     * O Ambiente evolui para um novo estado
     */
    public void evoluir();

    /**
     * O Ambiente gera um evento ao ser observado
     * @return Evento 
     */
    public Evento observar();

    /**
     * O Ambiente é executado consoante um comando específico
     * @param comando
     */
    public void executar(Comando comando);
}