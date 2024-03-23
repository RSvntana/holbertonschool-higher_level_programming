#!/usr/bin/python3
"""script that deletes all State objects with a name containing the letter a"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Setting up connection to the database
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create engine that connects to the core (MySQL)
    engine = create_engine(
        f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
    session.close()