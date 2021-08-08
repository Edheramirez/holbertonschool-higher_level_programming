#!/usr/bin/python3
"""file that contains the class definition of a City"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'
                .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()

    rows = session.query(City, State).\
        filter(City.state_id == State.id).all()

    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
