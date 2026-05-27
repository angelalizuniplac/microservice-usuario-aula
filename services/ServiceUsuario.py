from nameko_sqlalchemy import DatabaseSession
import db.db as db
from nameko.rpc import rpc
from db.ModelUsuario import Usuario

class ServiceUsuario:
    #Não é uma variavel. É um atributo de classe 
    # Quando o Nameko sobe o serviço, ele lê esse atributo e registra o serviço com esse nome na fila
    name = "service_usuario"

    db = DatabaseSession(db.Base)

    @rpc
    def AddUser(self, event):
        try:
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
            self.db.rollback()
            return {'erro': str(e)}
        finally:
            self.db.close()

    @rpc
    def UpdateUser(self, event):
        try:
            user = self.db.query(Usuario).filter(Usuario.id == event['id']).one()

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
            self.db.rollback()
            return {'erro': str(e)}
        finally:
            self.db.close()