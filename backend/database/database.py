import  sqlalchemy
import databases
import sqlalchemy.orm
import sqlalchemy.ext
import sqlalchemy.ext.declarative

database_addres = "mysql+pymysql://root:passwd1234@localhost:3306/socialnetwork"

_database = databases.Database(database_addres)
_metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(database_addres)
