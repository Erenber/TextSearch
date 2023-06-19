import datetime

from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field


class PyDoc(BaseModel):
    rubrics: str = Field(min_length=1, max_length=45)
    doc_text: str = Field(min_length=1)


Base = declarative_base()


class Docs(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    rubrics = Column(String(45), nullable=False)
    doc_text = Column(Text, nullable=False)
    created_date = Column(TIMESTAMP, default=datetime.datetime.utcnow)

    def __init__(self, py_doc):
        self.rubrics = py_doc.rubrics
        self.doc_text = py_doc.doc_text


metadata = Base.metadata


