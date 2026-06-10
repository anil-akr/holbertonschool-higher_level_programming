#!/usr/bin/python3
"""Script that prints all City objects from the database
hbtn_0e_14_usa, with their corresponding state name."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (session.query(State, City)
                      .filter(State.id == City.state_id)
                      .order_by(City.id)
                      .all())

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
