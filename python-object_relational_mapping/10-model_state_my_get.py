#!/usr/bin/python3
"""Script that prints the State object whose name matches
the argument from the database hbtn_0e_6_usa."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name_to_search = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (session.query(State)
                    .filter(State.name == state_name_to_search)
                    .first())
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
