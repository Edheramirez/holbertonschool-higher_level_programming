#!/usr/bin/python3
"""All states via SQLAlchemy"""


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
    results = session.query(State).all()

    for instance in results:
        print("{}: {}".format(instance.id, instance.name))

    session.close()
