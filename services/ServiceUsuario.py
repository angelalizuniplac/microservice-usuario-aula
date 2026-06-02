import db.db as database
from nameko.rpc import rpc, RpcProxy
from nameko_sqlalchemy import DatabaseSession
from db.ModelUsuario import Usuario
class ServiceUsuario:
    #Não é uma variavel. É um atributo de classe 
    # Quando o Nameko sobe o serviço, ele lê esse atributo e registra o serviço com esse nome na fila
    name = "service_usuario"

    db = DatabaseSession(database.Base)
    service_funcoes = RpcProxy("service_funcoes")

    @rpc
    def AddUser(self, event):
        try:
            if not self.service_funcoes.ValidaEmail(event['email']):
                raise Exception('email inválido')

            user = Usuario(nome=event['nome'], email=event['email'])
            self.db.add(user)
            self.db.commit()

            return {'id': user.id, 'nome': user.nome, 'email': user.email, 'msg': 'insert ok'}
        except Exception as e:
            self.db.rollback()
            return {'erro': str(e)}
        finally:
            self.db.close()

    @rpc
    def GetUser(self, event):
        try:
            user = self.db.query(Usuario).filter(Usuario.id == event['id']).one()

            return {'id': user.id, 'nome': user.nome, 'email': user.email, 'msg': 'get ok'}
        except Exception as e:
            return {'erro': str(e)}
        finally:
            self.db.close()

    @rpc
    def UpdateUser(self, event):
        try:
            user = self.db.query(Usuario).filter(Usuario.id == event['id']).one()

            if not self.service_funcoes.ValidaEmail(event['email']):
                raise Exception('email inválido')

            user.nome = event['nome']
            user.email = event['email']

            self.db.add(user)
            self.db.commit()

            return {'id': user.id, 'nome': user.nome, 'email': user.email, 'msg': 'update ok'}
        except Exception as e:
            self.db.rollback()
            return {'erro': str(e)}
        finally:
            self.db.close()

    @rpc
    def DeleteUser(self, event):
        try:
            user = self.db.query(Usuario).filter(Usuario.id == event['id']).one()

            self.db.delete(user)
            self.db.commit()

            return {'id': user.id, 'nome': user.nome, 'email': user.email, 'msg': 'delete ok'}
        except Exception as e:
            return {'erro': str(e)}
        finally:
            self.db.close()