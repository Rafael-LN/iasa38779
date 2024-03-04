package jogo.ambiente;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import ambiente.Ambiente;
import ambiente.Comando;
import ambiente.Evento;

public class AmbienteJogo implements Ambiente{

    private EventoJogo evento;
    private List<EventoJogo> eventos;
    
    public AmbienteJogo(){
        eventos = new ArrayList<EventoJogo>();
        eventos.add(EventoJogo.SILENCIO);
    }

    @Override
    public void evoluir() {
        eventos.add(gerarEvento());
    }

    @Override
    public Evento observar() {
        return evento;
    }

    @Override
    public void executar(Comando comando) {
        comando.mostrar();
    }

    private EventoJogo gerarEvento(){
        try (Scanner scanner = new Scanner(System.in)) {
            String s = scanner.nextLine();

            System.out.println(s);

            System.out.println(EventoJogo.valueOf(s.toUpperCase()));

            return EventoJogo.valueOf(s.toUpperCase());
        }
    }

    public EventoJogo getEvento(){
        return evento;
    }

}
