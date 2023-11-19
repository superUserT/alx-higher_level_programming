#!/usr/bin/python3

import sys

from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def Solution():
    """Prints the first State from the database."""
    # Creating database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Use the with to handle the close session
    with Session() as session:
        # Query the database for all states
        state = session.query(State).first()

        # Print the results
        if state is None or state == "":
            print("Nothing")
        else:
            print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    Solution()