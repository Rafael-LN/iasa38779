package jogo.ambiente;

import ambiente.Comando;

/**
 * Enumeração que representa os possíveis comandos do jogo.
 * Esta enumeração implementa a interface Comando, o que significa que cada Comando
 * desta enumeração é um comando que pode ser executado no jogo.
 * Implementa a interface Comando, garantindo que cada Comando possa ser mostrado.
 */
public enum ComandoJogo implements Comando {
    PROCURAR,
    APROXIMAR,
    OBSERVAR,
    FOTOGRAFAR;

    @Override
    public void mostrar() {
        System.out.println(this);
    }
    
}
