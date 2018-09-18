from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DB_CONNECT_STRING

engine = create_engine(DB_CONNECT_STRING)

Base = declarative_base()

class Dialog(Base):
    __tablename__ = 'dialogs'
    id = Column(Integer, primary_key=True)
    type = Column(String(10))
    auth = Column(String(20))
    content = Column(String(200))
    publish_time = Column(DateTime())

class TrainingData(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True)
    auth = Column(String(30))
    q_content = Column(String(80))
    a_content = Column(String(255))
    insert_time = Column(DateTime())

class FunctionData(Base):

    __tablename__ = 'function_data'
    id = Column(Integer, primary_key=True)
    type = Column(String(16))
    content = Column(String(255))
    effective_time = Column(DateTime())

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    #
    session=Session()
    #
    c = session.query(FunctionData).all()
    # for item in c:
    #     print(item.auth, item.q_content, item.a_content)

    # c = session.query(TrainingData).filter(TrainingData.a_content.like('%萧慧%')).all()
    # c = session.query(TrainingData).filter(TrainingData.a_content.like('%叼丝%')).all()
    # 青青姐姐
    for item in c:
        print(item.type, item.content)
        # session.delete(item)
    #
    # session.query(TrainingData).delete()
    session.commit()
    #


    # session.query(TrainingData).filter(TrainingData.a_content.like('%真一%')).delete()
    # c = session.query(TrainingData).filter(TrainingData.auth=='赵睿').all()
    # session.query(TrainingData).filter(TrainingData.auth=='赵睿').delete()
    # session.commit()
