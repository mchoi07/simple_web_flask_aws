from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('mysql+pymysql://Admin:techfieldbddb@techfield-0430.c48wltpqrvjo.us-east-2.rds.amazonaws.com:3306/testDB', convert_unicode=True)
metadata = MetaData(bind=engine)

users = Table('info', metadata, autoload=True)
con = engine.connect()
con.execute(users.insert(), firstname='Hello', lastname="goodbye", weight="135", height="5'7", age="138")