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

    public static void menu() {
        System.out.println("\n     \u001b[1;32m================================================\u001b[0m");
        System.out.println("     \u001b[1;32m|   Bem-vindo ao Explorador da Vida Selvagem!  |\u001b[0m");
        System.out.println("     \u001b[1;32m================================================\u001b[0m\n");
        System.out.println("+-------------------------------------------------------+");
        System.out.println("|                 \u001b[1;3mComandos disponíveis:\u001b[0m                 |");
        System.out.println("+-------------------------------------------------------+");
        System.out.println("| - \u001b[1;36mSilencio\u001b[0m: para aguardar em silêncio e observar.     |");
        System.out.println("| - \u001b[1;36mRuído\u001b[0m: para atrair a atençao e investigar.          |");
        System.out.println("| - \u001b[1;36mAnimal\u001b[0m: para observar um animal na proximidade.     |");
        System.out.println("| - \u001b[1;36mFuga\u001b[0m: para lidar com a fuga de um animal.           |");
        System.out.println("| - \u001b[1;36mFotografia\u001b[0m: para registrar a presença de um animal. |");
        System.out.println("| - \u001b[1;36mTerminar\u001b[0m: para sair do jogo.                        |");
        System.out.println("+-------------------------------------------------------+\n");

        System.out.println("+-------------------------------------------------------+");
        System.out.println("|       \u001b[1;3mNota\u001b[0m: Os comandos nao sao case sensitive        |");
        System.out.println("+-------------------------------------------------------+");


    }
    
    

    /**
     * Método principal que inicializa o ambiente, cria o personagem e inicia a execução do jogo.
     */
    public static void main(String[] args) {

        ambiente = new AmbienteJogo();
        personagem = new Personagem(ambiente);

        menu();
        executar();
        
    }
}
