package jogo.ambiente;

import java.util.ArrayList;
import java.util.List;
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
    private List<EventoJogo> eventos;
    
    /**
     * Inicializa a lista de eventos com um evento inicial.
     */
    public AmbienteJogo(){
        eventos = new ArrayList<EventoJogo>();
        eventos.add(EventoJogo.SILENCIO);
    }

    /**
     * Evolui o ambiente do jogo, gerando um novo evento.
     */
    @Override
    public void evoluir() {
        eventos.add(gerarEvento());
    }

     /**
     * Retorna o evento atual no ambiente.
     */
    @Override
    public Evento observar() {
        return evento;
    }

    /**
     * Executa um comando no ambiente do jogo.
     */
    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    /**
     * Gera um novo Evento com base no utilizador
     */
    private EventoJogo gerarEvento(){
        try (Scanner scanner = new Scanner(System.in)) {
            String s = scanner.nextLine();

            return EventoJogo.valueOf(s.toUpperCase());
        }
    }

    /**
     * Obtém o evento atual no ambiente do jogo.
     */
    public EventoJogo getEvento(){
        return evento;
    }

}
