#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create an engine that connects to the database
    db_engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}', pool_pre_ping=True)
    
    # Create the tables if they don't exist
    Base.metadata.create_all(db_engine)
    
    # Create a session to interact with the database
    Session = sessionmaker(bind=db_engine)
    db_session = Session()
    
    # Query the database to get all City objects along with their corresponding State names
    cities_with_states = db_session.query(City, State).join(State).all()
    
    # Print each city along with its state name
    for city, state in cities_with_states:
        print(f'{state.name}: ({city.id}) {city.name}')
    
    # Commit the changes
    db_session.commit()
