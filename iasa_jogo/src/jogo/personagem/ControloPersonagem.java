package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;

/**
 * Classe que implementa o controlo específico da personagem de um jogo.
 * Este controlo processa uma percepção e determina a acção a ser tomada com base nessa percepção.
 * Implementa a interface Controlo para definir o comportamento do controlo.
 */
public class ControloPersonagem implements Controlo {

    public ControloPersonagem(){}

    /**
     * Processa uma percepção recebida pelo agente e determina a acção a ser tomada com base nessa percepção.
     */
    @Override
    public Accao processar(Percepcao percepcao) {
        if (percepcao == null) {
            return null;
        }
        
        EventoJogo evento = (EventoJogo) percepcao.getEvento();

        evento.mostrar();

        ComandoJogo comandoJogo;
        
        switch (evento) {
            case RUIDO:
                comandoJogo = ComandoJogo.APROXIMAR;
                break;
                
            case ANIMAL:
                comandoJogo = ComandoJogo.OBSERVAR;
                break;

            case FOTOGRAFIA:
                comandoJogo = ComandoJogo.FOTOGRAFAR;
                break;
            default:
                comandoJogo = ComandoJogo.PROCURAR;
                break;
        }

        comandoJogo.mostrar();
        return new Accao(comandoJogo);

    }

    /**
     * Mostra o estado atual da personagem
     */
    private void mostrar(){}
    
}
