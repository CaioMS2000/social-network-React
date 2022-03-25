import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext
import sqlalchemy.ext.declarative

database_addres = "mysql+pymysql://root:passwd1234@localhost:3306/socialnetwork"
# engine = sqlalchemy.create_engine(database_addres, connect_args={"check_same_thread": False})
engine = sqlalchemy.create_engine(database_addres)
SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.ext.declarative.declarative_base()