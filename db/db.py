from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

STR_DATABASE = "mysql+pymysql://root:password@localhost:3306/abcBolinhas?charset=utf8"

engine = create_engine(STR_DATABASE)
Base = declarative_base()


# DatabaseSession resolve as conexões com o banco