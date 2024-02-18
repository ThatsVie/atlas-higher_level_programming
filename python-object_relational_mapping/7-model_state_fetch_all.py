#!/usr/bin/python3
"""
Script to list all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    db_engine = create_engine(
            f'mysql+mysqldb://{db_username}:{db_password}@localhost/{db_name}',
            pool_pre_ping=True
    )

    # Create all tables in the database
    Base.metadata.create_all(db_engine)

    # Create a session
    Session = sessionmaker(bind=db_engine)
    db_session = Session()

    # Query all State objects and order by id
    states = db_session.query(State).order_by(State.id).all()

    # Print the id and name of each State object
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    db_session.close()
