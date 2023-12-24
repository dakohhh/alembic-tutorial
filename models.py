from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker



Base = declarative_base()


class UserModel(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)

    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)

    birth = Column(DateTime)

    balance = Column(Integer, default=0, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)


    def __repr__(self):

        return f'<User: id={self.id}, first_name={self.first_name}, last_name={self.last_name}, balance={self.balance}, created_at={self.created_at}>'






# users =  [
#     UserModel(first_name="Wisdom", last_name="Dakoh", birth=datetime(2005, 3, 29)),
#     UserModel(first_name="Victor", last_name="Dakoh", birth=datetime(2006, 11, 22))
# ]


session_maker = sessionmaker(bind=create_engine("sqlite:///models.db"))
 

# def create_users():

#     with session_maker() as session:

#         for user in users:
#             session.add(user)

#         session.commit()


with session_maker() as session:

    user_records = session.query(UserModel).all()

    for user in user_records:

        print(type(user.balance))




