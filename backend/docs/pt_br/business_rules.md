## Tests (Provas)
   1. Um time pode ter no máximo 3 provas. Para facilitar, quem é responsável por essa restrição é o backend. Verifica-se se o time já possui três provas registradas, se tiver, não é mais possível registrar provas. 
   2. A penalidade é aplicável apenas a segunda prova (Velocidade máxima)
   3. O valor da penalidade é acrescentado ao valor do campo principal da prova (distância percorrida, tempo feito, peso retentor). Já que a penalidade é usada apenas na prova "Velocidade máxima", o valor é adicionado ao "Tempo feito". 
      - A penalidade foi pensado para ser usado em mais casos, mesmo que nossa regra de negócio não a use, ele poderia ser usado para a prova "Tração", mas nesse caso a penalidade teria um valor negativo pois quanto maior o valor do "Peso rententor", maior será a pontuação da equipe. 

## Squads (Times)
   1. Cada equipe possui um grupo de estudantes associado. A nota é associada a equipe, ou seja, todos os estudantes da equipe possuem a mesma nota.
   2. O carro é associado à equipe.
   

## Students (Estudantes)
   1. RA é a identificação do estudante (um valor uníco)