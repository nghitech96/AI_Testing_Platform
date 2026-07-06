from sqlalchemy import Column, Integer, String
from database.db import Base


class EvaluationRun(Base):
    __tablename__ = "evaluation_runs"

    id = Column(Integer, primary_key=True, index=True)
    dataset = Column(String)
    model = Column(String)