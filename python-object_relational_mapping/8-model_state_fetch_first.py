#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create an engine that connects to the database
    db_username = argv[1]
    db_password = argv[2]
    db_name = argv[3]
    engine = create_engine(
      f'mysql+mysqldb://{db_username}:{db_password}@localhost:3306/{db_name}',
      pool_pre_ping=True
    )
    
    # Create tables in the database if they don't exist
    Base.metadata.create_all(engine)
    
    # Create a sessionmaker object bound to the engine
    Session = sessionmaker(bind=engine)
    
    # Create a session to interact with the database
    db_session = Session()
    
    # Query the database to get the first State object
    first_state = db_session.query(State).order_by(State.id).first()
    
    # Check if a State object was found
    if first_state is not None:
        # Print the id and name of the State object
        print(f'{first_state.id}: {first_state.name}')
    else:
        # Print a message if no State object was found
        print('Nothing')
