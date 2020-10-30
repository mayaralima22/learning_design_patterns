#Facade
O facade é um padrão de projeto estrutural, que tem como ideia simplificar
 uma lib, framework ou qualquer conjunto complexo de classes.

##Problema que o facade soluciona:
Quando precisamos utilizar uma lib ou um framework, que a implementação seria
complexa, com diversas dependências, métodos, etc.

Como resultado, a lógica de negócio de suas classes vai ficar 
firmemente acoplada aos detalhes de implementação das classes de terceiros, 
tornando difícil compreendê-lo e mantê-lo.

##Benefício usando facade:
Ao utilizar o facade, que é uma espécie de fachada, criamos uma 
interface simples para aquele subsistema complexo. Ou melhor, pegamos essa
biblioteca complexa e organizamos tudo que será necessário para o nosso 
sistema, visto que este não utiliza todos os métodos da biblioteca.

##Analogia:
Quando você liga para uma loja para fazer um pedido, um operador é sua 
fachada para todos os serviços e departamentos da loja. 
O operador fornece a você uma simples interface de voz para o sistema 
de pedido, pagamentos, e vários sistemas de entrega.

##Referências:
- [Teoria Facade](https://refactoring.guru/pt-br/design-patterns/facade)
- [Aplicação de código](https://medium.com/@hnmpatel/design-patterns-in-python-facade-65b8a393ff68)