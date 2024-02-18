#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as an argument from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create an engine to connect to the database
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    # Create tables in the database if they don't exist
    Base.metadata.create_all(db_engine)

    # Create a session maker bound to the engine
    Session = sessionmaker(bind=db_engine)

    # Create a session to interact with the database
    db_session = Session()

    # Get the name of the state from the command-line argument
    state_name = sys.argv[4]

    # Query the database to get the State object with the specified name
    state = db_session.query(State).filter(State.name == state_name).first()

    # Check if the State object was found
    if state is None:
        print("Not found")
    else:
        # Print the ID of the State object
        print(state.id)
