# Execução dos serviços locais. 


## Requisitos: 

1. Baixar imagem do mySql para rodar em docker: 

    ```docker run -e MYSQL_ROOT_PASSWORD=password -p 3306:3306 --name mysql --restart unless-stopped -d mysql:9```

Configurar a base:
2.  Usar o cliente MySQL dentro do container, no terminal execute:

```docker exec -it mysql mysql -u root -p```

3. Nesse mesmo terminal crie um novo banco de dados chamado 'abcBolinhas':

    ```create database abcBolinhas;```

4. Baixe a imagem do RabbitMQ para rodar em docker:

 ```docker run -d --restart=always --hostname rabbitmq --name rabbitmq -p 8080:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password rabbitmq:4.3-management-alpine```

# Ambiente virtual 

1. Criar um ambiente virtual para isolar o projeto: (Ver observação de versões)

    ```python -m venv venv```

2. Ativar o ambiente:

    ```venv\Scripts\activate```

3. Instalar a biblioteca Nameko e outras necessárias: 


    ```python -m pip install --upgrade pip setuptools``` 
    
    Obs: Devido as compatibilidades de versão você precise compatibilizar a versão do setuptools: `pip install "setuptools<71"`

    #Framework de microsserviços para Python baseado em RabbitMQ/AMQP:

    ```pip install nameko```

    #mapeia objetos relacionais para Python (mapeia tabelas do banco em classes Python) - sem escrever SQL puro:

    ```pip install sqlalchemy```

    #gerenciamento de sessões e conexões do banco dentro dos serviços:

    ```pip install nameko_sqlalchemy```

    #Permite conectar aplicações Python ao MySQL:

    ```pip install pymysql```

    #Biblioteca de criptografia Necessária para SSL/TLS, autenticação segura e alguns drivers/bibliotecas:

    ```pip install cryptography```


# Execução do serviço de usuario

A execução precisa ser realizada através do Nameko

1. Executar através do Nameko: 

Se na raiz: 
 ```nameko run ServiceUsuario --config config.yaml```

 Se organizado em pastas como é o caso desse projeto: 
 `nameko run services.ServiceUsuario --config config/config.yaml`

# Testes

1. Em um novo terminal, execute o comando abaixo para abrir um shell nameko (não esqueça do venv):
 ```nameko shell --config config/config.yaml```

2. No mesmo terminal, para fazer chamadas rcp e testar o serviço execute um por vez:

```
>>> n.rpc.service_usuario.AddUser(event={'id': '0', 'nome': 'Sistemas Distribuídos', 'email': 'abc@123.com'})

>>> n.rpc.service_usuario.AddUser(event={'id': '0', 'nome': 'teste 18/11', 'email': 'bolinhas@123'})

>>> n.rpc.service_usuario.UpdateUser(event={'id': '2', 'nome': 'seuNome', 'email': 'seuNome@123'})

>>> n.rpc.service_usuario.DeleteUser(event={'id': '1'})

>>> n.rpc.service_usuario.GetUser(event={'id': '2'})

>>> n.rpc.service_usuario.GetUser(event={'id': '1'}) 
```

3. Caso queira verificar direto no banco de dados (terminal): 

`docker exec -it mysql mysql -u root -p`

 `use abcBolinhas;`

 `select * from tb_usuario;`


# Extras 
- Verificar IP dos containers: 

 ```docker inspect -f "{{.NetworkSettings.IPAddress}}" mysql```

--------

# Versões Python 
Nameko ainda não tem suporte com versões do python 3.12+, então vamos precisar gerar o nosso ambiente virtual com a versão compativel, 3.11. 


1. Baixe e instale o python 3.11 https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
Importante: NÃO marque a opção "Add to PATH", dessa forma não interfere na versão do seu SO. 

2. Aqui temos algumas alternativas: 
- No terminal execute o comando: `where.exe py`  
 Se aparecer algo como "C:\Windows\py.exe", voce pode executar o comando direto: `py -3.11 -m venv venv`

- Se não aparecer o mencionado acima, você deve localizar onde foi instalado, o comando pode te ajudar: `where.exe python`. E
Localizando o caminho onde foi instalar a versão 3.11 voce pode criar o ambiente virtual apontando para a versão 3.11: 
 `"C:\Program Files\Python311\python.exe" -m venv venv  ` 

Ambiente criado na versão 3.11 do python, agora pode seguir normalmente  


