# Solução adotada para o desafio


## Etapas
1. Interpretação, contexto e levantamento de requisitos para o domínio do problema;
    1. Criação de ostras, a temperatura do mar é algo crítico.
    1. Broker MQTT? https://engprocess.com.br/mqtt-broker/ , razoalvemente e em alto nível um sistema de publish-subscriber para notificações.
    1. Separar a fazenda de ostras por (filtros): nome, data, temp, localidade, owner.
1. Mapeamento do domínio do problema para um MER.
    1. ![Mapeamento Conceitual](images/modelo-conceitual.png)
    1. ![Mapemaneto Lógico](images/modelo-logico.png)
1. Desenvolvimento da aplicação

## Respostas
1. __Código:__ _OBS_: Supondo que bd seja uma função nativa para manipular o banco de dados, supondo que findData é uma função nativa para localizar data em uma string e supondo que a função sendSMS envia um SMS para o número (primeiro paramentro) e a mensagem (segundo parametro).
```python
# Conecta BD e executa query
def getBD(query):
    try:
        connection = bd.connect()
        result = connection.execute(query)
        connection.close()
        return result
    except (Exception, error) as error:
        print(Error)

# Insere os dados coletados para o BD
def insertBD(idFazenda, data, temperatura):
    query = "INSERT INTO Historico (idFazenda, data, temperatura) VALUES (idFazenda, data, temperatura)"
    return getBD(query)
        
# Recebe Alertas do broker MQTT (dispositivo IoT)
def recebeAlertas(data, temperatura, idFazenda):
    result = insertBD(idFazenda, data, temperatura)
    if result is null:
        raiseException("Error, dado não inserido no BD")
    if(temp > 22):
        sendAlert('[CRITÍCO] Temperatura acima de 22°C, STRESS ostras', idFazenda)
    elif(temp > 31):
        sendAlert('[FATAL] Temperatura acima de 31°C, ostras em óbito', idFazenda)
    else:
        publish(idFazenda, '[NORMAL] Temperatura mensurada '+tempetura+'°C')

# Envia Alerta ao proprietário por SMS e Publica         
def sendAlert(string, idFazenda):
    findOwner = getBD('SELECT idPessoa FROM Fazenda where id = '+idFazenda)
    query = 'SELECT a.nome, a.telefone FROM Pessoas as a WHERE a.CPF = '+findOwner+'"'
    result = getBD(query)
    sendSMS = (result[1],'Olá Sr. '+result[0]+'A fazenda'+idFazenda+' está com o seguinte alerta: '+string)
    publish(idFazenda, string)

# Publica o alerta em um arquivo monitorado
def publish(idFazenda, string):
    os.system('echo idFazenda+" "+string >> file')

# Monitora o arquivo
def monitora(idFazenda, last):
    lastLine = os.system("awk '/./{line=$0} END{print line}' file")
    if idFazenda is in lastLine:
        if findData(lastLine) > data(last):
            raise(Atualização)

# Acessa historico
def historico(idFazenda, nome, data, temperatura, localidade, idPessoa)
    query = "SELECT a.nome,a.localidade,b.data,b.temperatura,c.idPessoa FROM Fazenda as a, Historico as b, Pessoa as c WHERE a.id = b.idFazenda and a.idPessoa = c.CPF"
    if idFazenda is not None: query + " and a.idFazenda = "+ idFazenda
    if nome is not None: query + " and a.nome = "+ nome
    if data is not None: query + " and b.data = "+ data
    if temperatura is not None: query + " and b.temperatura = "+ temperatura
    if localidade is not None: query + " and a.localidade = "+ localidade
    if idPessoa is not None: query + " and c.CPF = "+ idPessoa
    print getBD(query)
```

2. __Diagramas de fluxo da aplicação__

3. __Tecnologias e motivação__
R: Possivelmente para esta solução adotaria uma linguaguem dinamicamente tipada como Python, pois a curva de desenvolvimento seria rápida. Para as consultas  utilizaria um banco de dados relacional PostgreSQL visto que o domínio do problema não implica em soluções Big Data, ainda observando que o fato da temperatura é um dado vital (>31°C) e implicaria em um grande prejuizo, as propriedades ACID são necessárias.
