#!/usr/bin/python3
"""
Script that adds the State object Louisiana to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine to connect to the database
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                               sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)

    # Create tables in the database if they don't exist
    Base.metadata.create_all(db_engine)

    # Create a session maker bound to the engine
    Session = sessionmaker(bind=db_engine)

    # Create a session to interact with the database
    db_session = Session()

    # Create a new State object with the name 'Louisiana'
    state = State(name="Louisiana")

    # Add the State object to the session
    db_session.add(state)

    # Commit the changes to the database
    db_session.commit()

    # Print the ID of the newly added State object
    print(state.id)
