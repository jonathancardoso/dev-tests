# Desafio para desenvoledores (_hipoteticamente_)
Este repo faz parte (_hipoteticamente_) de um processo de seleção para uma vaga de desenvolvedor.
Sendo assim, este repo serve para rastrear as medidas adotadas, tipos de solução e tempo decorrido.

## Descrição
Como próxima etapa do processo seletivo para a vaga de Desenvolvedor Python, você precisará executar um teste, que tem o objetivo de verificar o fit técnico para a vaga.
1. Criar um servidor http (flask, django, bottle, etc) contendo 2 serviços:
    1. _Login_ (username, password).
        1.  pode ser hardcoded o usuário/senha.
    1. _Upload (file)_
        1. salvar o arquivo no diretório `uploads` junto do código do serviço http python.
1. Criar um app escrito em Python utilizando PyQt ou PySide (preferencialmente) contendo as seguintes funcionalidades:
    1. Tela de login (consumir o serviço criado anteriormente)
    1. Na tela principal:
    1. tem que ter um botão para selecionar um arquivo do sistema e outro botão para realizar o upload.
    1. tem que ter uma área destinada a lista de arquivos sendo feito o upload, a barra de progresso e uma previsão de término.
    1. deverá haver uma opção para cancelar o upload.
    1. O aplicativo deverá estar sempre disponível no trackbar do windows (mesmo quando o aplicativo for fechado pela janela principal).
    1. deverá haver um menu no trackbar do windows com a possibilidade de fechar o aplicativo.
1. Deverá ser criado o arquivo de dependências _requirements.txt_ com as dependências utilizadas.
    1. Pode ser omitido a etapa de instalação do python e suas dependências (QT, PyQT ou PySide).
1. Deverá ser entregue o código com um arquivo _README.md_ com as instruções de execução.

## Solução
Para desenvolvimento dessas aplicações foi utilizado: __Python, Flask, PyQT4, PySide, sqlAchemy (sqlite), Json, Werkzeug__ .
O arquivo de dependências foi gerado através do __pipreqs__.

### Setup
Para executar essa aplicação, certifique-se que você possui todos as bibliotecas necessárias.
```
pip install -r requirements.txt
```
Para iniciar a aplicação, é necessário realizar o setup de inicialização para gerar o banco de dados.
``` make setup ``` ou simplesmente ``` python tabledef.py; python dummy.py ```

### Execução
Para executar a aplicação é necessário inicializar os serviços ```__python app.py__``` e após ```__python browser.py__``` para visualizar a aplicação.

### Informações
Os serviços requeridos no item 1 deste desafio estão desenvolvidos em __controller.py__.
O arquivo __app.py__ é responsavél pelo roteamento das URL's e a view da aplicação.
Para contemplar as necessidades descritas no item 2 deste desafio, foi implementado em __browser.py__ as funções para visualização da aplicação e integração ao desktop.

1. Para limpar os arquivos enviados ao servidor: ```make cleanData```
1. Para limpar o banco de dados: ```make cleanDB```
1. Para resetar a aplicação ao estado inicial: ```make clean```
