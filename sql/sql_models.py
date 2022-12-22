from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sqla

Base = declarative_base()


class AppData(Base):
    __tablename__ = 'appdata'

    id = sqla.Column(sqla.Integer, primary_key=True)
    category = sqla.Column(sqla.String(64), nullable=False)
    data = sqla.Column(sqla.String(64), nullable=False)

    def __repr__(self):
        return f"Id: {self.id} , Category: {self.category}, Data: {self.data}"

