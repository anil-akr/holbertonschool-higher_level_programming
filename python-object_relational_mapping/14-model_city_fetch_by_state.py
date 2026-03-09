#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa,
in the format <state name>: (<city id>) <city name>.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./14-model_city_fetch_by_state.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities joined with states, ordered by cities.id
    cities = session.query(City, State).join(State, City.state_id == State.id)\
        .order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
