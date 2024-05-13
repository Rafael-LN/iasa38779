from plan.plano import Plano


class PlanoPEE(Plano):
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]
        
    def obter_accao(self, estado):
        """
        Se houver passos
            Retirar o passo de passos
            Se passo for igual a estado
            Retorna o operador do passo
        """
        if self.__passos:
            passo = self.__passos.pop()
            if passo.estado == estado:
                return passo.operador
    
    def mostrar(self, vista):
        """
        Mostrar 
        
        """
        if self.__passos:
            # Mostrar passos do plano como vectores
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)