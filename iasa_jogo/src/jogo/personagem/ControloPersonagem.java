package jogo.personagem;

import agente.Accao;
import agente.Controlo;
import agente.Percepcao;
import ambiente.Evento;
import jogo.ambiente.ComandoJogo;
import jogo.ambiente.EventoJogo;
import maqest.Estado;
import maqest.MaquinaEstados;

/**
 * Classe que implementa o controlo específico para personagens de um jogo, usando uma máquina de estados.
 * Esta classe define as transições de estados e as ações associadas com base nas percepções recebidas pela personagem.
 * Implementa a interface Controlo para definir o comportamento do controlo da personagem.
 */
public class ControloPersonagem implements Controlo {

    private MaquinaEstados maqEst;
    private Estado estado;

    /**
     * Construtor padrão que inicializa a máquina de estados e define as transições de estados.
     */
    public ControloPersonagem() {

        Estado procura = new Estado("Procura");
        Estado inspeccao = new Estado("Inspecao");
        Estado observacao = new Estado("Observacao");
        Estado registo = new Estado("Registo");

        procura.transicao(EventoJogo.ANIMAL, observacao, new Accao(ComandoJogo.APROXIMAR));
        procura.transicao(EventoJogo.RUIDO, inspeccao, new Accao(ComandoJogo.APROXIMAR));
        procura.transicao(EventoJogo.SILENCIO, procura);

        inspeccao.transicao(EventoJogo.ANIMAL, observacao, new Accao(ComandoJogo.APROXIMAR));
        inspeccao.transicao(EventoJogo.RUIDO, inspeccao, new Accao(ComandoJogo.PROCURAR));
        inspeccao.transicao(EventoJogo.SILENCIO, procura);

        observacao
                .transicao(EventoJogo.FUGA, inspeccao);
        observacao.transicao(EventoJogo.ANIMAL, registo, new Accao(ComandoJogo.OBSERVAR));

        registo
                .transicao(EventoJogo.ANIMAL, registo, new Accao(ComandoJogo.FOTOGRAFAR));
        registo.transicao(EventoJogo.FUGA, procura);
        registo.transicao(EventoJogo.FOTOGRAFIA, procura);

        estado = procura;
        maqEst = new MaquinaEstados(estado);

    }

    /**
     * Obtém o estado atual da personagem.
     */
    public Estado getEstado() {
        return estado;
    }

    /**
     * Processa uma percepção recebida pelo agente e determina a ação a ser tomada com base nessa percepção.
     * @param percepcao A percepção recebida pelo agente.
     * @return A ação a ser realizada com base na percepção, ou null se não houver ação a ser realizada.
     */
    @Override
    public Accao processar(Percepcao percepcao) {
        if (percepcao == null) {
            return null;
        }

        Evento evento = percepcao.getEvento();

        Accao accao = maqEst.processar(evento);

        estado = maqEst.getEstado();

        mostrar();

        return accao;
    }

    /**
     * Mostra o estado atual da personagem
     */
    private void mostrar() {
        System.out.println("Estado: " + getEstado().nome);
    }

}
