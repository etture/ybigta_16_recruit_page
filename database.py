import sys

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    phone_num = Column(String(100), nullable=False)

    @property
    def serialize(self):
        return {
            'phone_num': self.phone_num
        }

engine = create_engine('sqlite:///contacts-collection.db')
Base.metadata.create_all(engine)