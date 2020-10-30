#Observer

Permitir que um objeto seja capaz de notificar outro objeto. 
Ou melhor, quando um objeto mudar de estado, todos os seus "dependentes" 
são notificados e atualizados automaticamente. 



#Pub/Sub
Ter um centralizador de mensagens, dessa forma, dá pra filtrar quem recebe que tipo de mensagem
e de quem. Esse centralizador normalmente é chamado de bus. 
Utilizando sistema de eventos como Redis, RabbitMQ, etc...



##Referências:
- [Teoria sobre o observer (Refactoring.guru)](https://refactoring.guru/pt-br/design-patterns/observer)
- [Vídeo no Youtube explicando sobre observer e pub/sub](https://www.youtube.com/watch?v=sbCJucr8aJg&list=PLOQgLBuj2-3IPHFlBmqhtbM4vLJg9tob4&index=4)