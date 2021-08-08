#!/usr/bin/python3
"""lists all State Contains a"""


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
    state = session.query(State).order_by(State.id).first()

    for state in session.query(State).filter(State.name.like('%a%'))\
            .order_by(State.id).all():

        print("{}: {}".format(state.id, state.name))
    session.close()
