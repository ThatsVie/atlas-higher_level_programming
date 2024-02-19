#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
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
  
  # Query the database for all State objects with names containing 'a'
    states_to_delete = db_session.query(State).filter(State.name.like('%a%')).all()

    # Delete the queried State objects
    for state in states_to_delete:
        db_session.delete(state)
    
    # Commit the changes to the database
    db_session.commit()

# Close session
    db_session.close()  
