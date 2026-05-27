from db.db import Base, engine
from sqlalchemy import Column, Integer, VARCHAR

class Usuario(Base):
    __tablename__ = "tb_usuario"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(100), nullable=False)

Base.metadata.create_all(engine)

# define o que é um Usuário e como ele vira uma tabela no banco.    