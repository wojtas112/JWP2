from sqlalchemy import create_engine, Column, Integer, String, text, Float
from sqlalchemy.orm import declarative_base, Session


engine = create_engine('sqlite+pysqlite:///:memory:', echo=True, future=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)

Base.metadata.create_all(engine)

with Session(engine) as session:
    new_user = User(name="Jan Kowalski", age=30)
    session.add(new_user)
    session.commit()

with Session(engine) as session:
    new_user = User(name="Andrzej Bednarek", age=15, grade=5)
    session.add(new_user)
    session.commit()

with Session(engine) as session:
    new_user = User(name="Anna Młynarczyk", age=22, grade=4)
    session.add(new_user)
    session.commit()

with Session(engine) as session:
    users = session.execute(text("SELECT * FROM students")).all()
    for user in users:
        print(f'{user.name}, {user.age}, {user.grade}')

with Session(engine) as session:
    user_to_update = session.get(User, 1) # Zalóżmy, że rekord z ID 1 istnieje
    if user_to_update:
        user_to_update.name = "Jan Nowak"
        session.commit()

with Session(engine) as session:
    user_to_delete = session.get(User, 1)
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()