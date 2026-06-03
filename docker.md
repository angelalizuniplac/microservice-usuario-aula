Gerando imagem docker 

1. Requisitos: RabbitMq, mysql e o serviço de funções. Verifique se todos estão executando corretamente.  

2. Verifique qual ip está executando os container rabbitMQ e MySql, através dos comandos:
`docker inspect -f "{{.NetworkSettings.IPAddress}}" rabbitmq`

 `docker inspect -f "{{.NetworkSettings.IPAddress}}" mysql`

3. Altere o localhost para os IPs correspondentes ao docker.

4. Rode o build do docker para criar a imagem Ps: não esqueça do ponto no final . que indica que o dockerfile está no diretorio atual.  
` docker build -t microservice_usuario . `

5. Com isso confira que a imagem já está criada e você pode executar o container do serviço localmente. 

-----------
# Enviando para o repositorio

1. Faça autenticação local com o seu repositorio do docker hub(Se ja estiver autenticado pule esse passo)

Exemplo do meu:  `docker login --username=angeladlizuniplac` 

2. Com a imagem criada, gere a tag(versionamento):

`docker tag microservice_usuario angeladlizuniplac/microservice_usuario`

Geramos a imagem para testar localmente, mas também é possível gerar a imagem e a tag ao mesmo tempo: `docker build -t angeladlizuniplac/microservice_usuario .  `

3. Faça o push das imagens para o repositorio docker:
`docker push angeladlizuniplac/microservice_usuario`

----
<br>

# Baixar a imagem do repositório

`docker run -d -it --name serviceUsuario angeladlizuniplac/microservice_usuario`

---
<br>

# Testar
1. Qualquer terminal não precisamos mais usar o venv local

 `docker exec -it serviceUsuario nameko shell --config config/config.yaml`

2. Excute os comandos RPC que desejar como por exemplo:
  `n.rpc.service_usuario.AddUser(event={'id': '0', 'nome': 'Sistemas Distribuídos', 'email': 'abc@123'})  `

  ---

  # Escalonamento

  Caso necessite subir mais de um serviço baseado na mesma imagem:
`docker run -d -it --name serviceUsuario2 angeladlizuniplac/microservice_usuario`