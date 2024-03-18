package jogo.ambiente;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.Scanner;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

/**
 * Classe que representa o ambiente do jogo.
 * Esta classe controla a evolução do ambiente do jogo, gera eventos e permite que a personagem
 * observe e execute comandos no ambiente.
 * Implementa a interface Ambiente para definir o comportamento do ambiente.
 */
public class AmbienteJogo implements Ambiente{

    private EventoJogo evento;
    private Map<String, EventoJogo> eventos;
    
    /**
     * Construtor padrão que inicializa o ambiente do jogo com um evento inicial.
     * Inicializa também a lista de eventos disponíveis.
     */
    public AmbienteJogo(){
        evento = EventoJogo.SILENCIO;

        eventos = new HashMap<String, EventoJogo>();
        eventos.put("SILENCIO", EventoJogo.SILENCIO);
        eventos.put("RUIDO", EventoJogo.RUIDO);
        eventos.put("ANIMAL", EventoJogo.ANIMAL);
        eventos.put("FUGA", EventoJogo.FUGA);
        eventos.put("FOTOGRAFIA", EventoJogo.FOTOGRAFIA);
        eventos.put("TERMINAR", EventoJogo.TERMINAR);
    }

    /**
     * Evolui o ambiente do jogo, gerando um novo evento.
     */
    @Override
    public void evoluir() {
        evento = gerarEvento();
    }

     /**
     * Mostra e retorna o evento atual quando o ambiente é observado.
     */
    @Override
    public Evento observar() {
        evento.mostrar();
        return evento;
    }

    /**
     * Executa um comando no ambiente do jogo, mostrando o comando executado.
     */
    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    /**
     * Gera um novo Evento com base no utilizador
     */
    private EventoJogo gerarEvento(){
        Scanner scanner = new Scanner(System.in);
        EventoJogo novoEvento = null;

        do {
            System.out.println("\nEvento?");
            String eventoPretendido = scanner.nextLine();
            System.out.println();
            novoEvento = eventos.get(eventoPretendido.toUpperCase());

            if (novoEvento == null) {
                System.out.println("\u001B[1;31mEvento inválido.\u001B[0m");
            }
            
        } while (novoEvento == null);

        return novoEvento;
        
    }

    /**
     * Obtém o evento atual no ambiente do jogo.
     */
    public EventoJogo getEvento(){
        return evento;
    }

}
