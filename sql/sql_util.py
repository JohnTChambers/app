import os

from typing import Union

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_connection_string() -> str:
    """
    returns the connection string from the environment

    :return: connection string
    """
    return os.environ.get("SNEK_CONNECTION_STRING")

def set_up_session(connection_string) -> Union[sessionmaker, create_engine]:
    """
    Return a session object using for a particular database connection using SQLAlchemy

    :param connection_string: connection string
    :return: None
    """
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine

def loop_through_records(session, table):
    """
    loop through records and print them

    :param session: session object
    :return: None
    """
    for record in session.query(table).all():
        print(record)

def add_record(session, table, record):
    """
    add a record to the database

    :param session: session object
    :param table: table object
    :param record: record object
    :return: None
    """
    session.add(record)
    session.commit()