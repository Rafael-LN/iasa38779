package jogo.personagem;

import agente.Agente;
import jogo.ambiente.AmbienteJogo;
/**
 * Classe que representa uma personagem no jogo.
 * Uma personagem é um Agente que possui um Ambiente de jogo e um controlo específico da personagem.
 */
public class Personagem extends Agente {

    /**
     * Construtor para criar uma nova personagem com o ambiente de jogo especificado.
     */
    public Personagem(AmbienteJogo ambiente) {
        super(ambiente, new ControloPersonagem());
    }
    
}
