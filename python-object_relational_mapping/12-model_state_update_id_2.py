#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the database
    db_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                              sys.argv[1], sys.argv[2], sys.argv[3]), 
                              pool_pre_ping=True)

    # Create the necessary tables if they don't exist
    Base.metadata.create_all(db_engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=db_engine)
    db_session = Session()

    # Query the database for the State object with id 2
    state = db_session.query(State).filter_by(id=2).first()

    # Change the name of the State object
    state.name = "New Mexico"

    # Commit the changes to the database
    db_session.commit()

    # Close session
    db_session.close()
