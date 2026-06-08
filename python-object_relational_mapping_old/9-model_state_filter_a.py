#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: ./9-model_state_filter_a.py "
            "<username> <password> <database>"
        )
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Création de l’engine SQLAlchemy
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération des States contenant 'a', triés par id
    states = session.query(State).filter(State.name.like("%a%")).order_by(
        State.id
    ).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
