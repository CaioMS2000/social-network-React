database_addres = "mysql+pymysql://root:passwd1234@localhost:3306/socialnetwork"

#Ormar
import  sqlalchemy
import databases
import ormar


database = databases.Database(database_addres)
metadata = sqlalchemy.MetaData()
# engine = sqlalchemy.create_engine(database_addres)

# just SQLAlchemy
"""
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext
import sqlalchemy.ext.declarative

engine = sqlalchemy.create_engine(database_addres)
SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = sqlalchemy.ext.declarative.declarative_base()
"""