#!/usr/bin/python3
"""changes the name of a State object from the database"""


import sys
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3],
                        pool_pre_ping=True))

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter(State.id == 2).all()
    if states:
        states[0].name = "New Mexico"

    session.commit()
    session.close()
