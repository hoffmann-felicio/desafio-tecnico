# desafio-tecnico

O código para abordar o problema especificado foi dividido em modulos com resposabilidades especificas.

O módulo Familias é responsavel por definir os atributos relacionados à uma familia (id, status, renda, pessoas) e oferece métodos para calcular informações relativas a esses dados (renda total, idade, dependentes).

O módulo Parser é responsável por abrir os arquivos da pasta DB (representando um banco de dados com as familias) e extrair as informações das familias dos JSON.

O módulo Classificador é resposável pelas regras de negócio e proporcionar a listagem seguindo essas regras.

O módulo Main é responsável por juntar todas essas classes e obter as listagem desejada.


A implementação foi feita tendo em mente uma separação de responsabilidades em vários módulos de forma a não sobrecarregar um único modulo com responsabilidades demais e também a facilitar extensões. Em relação a escolha de armazenamento das familias, escolhi utilizar vários arquivos JSON pois foi a opção apresentada e então foi mais prático e ágil para adicionar novas familias, no entendo o código pode ser refatorado para outra abordagem de armazenamento sem prejuicar os demais módulos.