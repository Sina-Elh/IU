from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///assignment.db')
Session = sessionmaker(bind=engine)
session = Session()


class TrainingData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True)
    x = Column(float)
    for i in range(1, 4):
        locals()[f'y{i}'] = Column(float)


class IdealFunctions(Base):
    __tablename__ = 'ideal_functions'
    id = Column(Integer, primary_key=True)
    x = Column(float)
    for i in range(1, 51):
        locals()[f'y{i}'] = Column(float)


class TestData(Base):
    __tablename__ = 'test_data'
    id = Column(Integer, primary_key=True)
    x = Column(Float)
    y = Column(Float)
    delta_y = Column(Float)
    ideal_func_no = Column(Integer)


def init_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()