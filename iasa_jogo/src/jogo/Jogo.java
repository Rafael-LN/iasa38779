package jogo;

import jogo.ambiente.AmbienteJogo;
import jogo.ambiente.EventoJogo;
import jogo.personagem.Personagem;

/**
 * Classe principal que representa o jogo.
 * Esta classe controla a execução do jogo, evoluindo o ambiente e
 * fazendo com que o personagem execute acções até que o evento de TERMINAR ocorra.
 */
public class Jogo {

    /**
     * O Jogo tem um ambiente e uma personagem
     */
    private static AmbienteJogo ambiente;
    private static Personagem personagem;
    
    /**
     * O jogo continua a ser executado até que o evento de TERMINAR ocorra no ambiente.
     */
    public static void executar(){
        while (ambiente.getEvento() != EventoJogo.TERMINAR) {
            ambiente.evoluir();
            personagem.executar();
        }
    }

    /**
     * Método principal que inicializa o ambiente, cria o personagem e inicia a execução do jogo.
     */
    public static void main(String[] args) {

        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);

        executar();
        
    }
}
