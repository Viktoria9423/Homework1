from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"

engine = create_engine(DATABASE_URL)

connection = engine.connect()
print("Подключение успешно!")
connection.close()
