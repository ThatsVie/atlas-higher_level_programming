#!/usr/bin/python3
"""
Script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
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
  
    # Query the database to get all State objects containing the letter 'a'
    states_with_a = db_session.query(State).filter(State.name.like('%a%'))\
                                           .order_by(State.id).all()
  
    # Print the id and name of each State object
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
