#!/usr/bin/python3
"""script that lists all city objects"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for obj in session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).order_by(City.id):
        print(f"{obj[0]}: ({obj[1]}) {obj[2]}")
