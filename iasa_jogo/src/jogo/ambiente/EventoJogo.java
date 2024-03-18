package jogo.ambiente;

import ambiente.Evento;

/**
 * Enumeração que representa os possíveis eventos do jogo.
 * Cada Evento desta enumeração é um tipo de evento que pode ocorrer durante o jogo.
 * Implementa a interface Evento, garantindo que cada Evento possa ser mostrado.
 */
public enum EventoJogo implements Evento {
    SILENCIO,
    RUIDO,
    ANIMAL,
    FUGA,
    FOTOGRAFIA,
    TERMINAR;

    @Override
    public void mostrar() {
        System.out.println("Evento: " + this.name());
    }
}
