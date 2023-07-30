#!/usr/bin/python3
"""update state name"""


if __name__ == "__main__":
    import sys
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    obj = session.query(State).filter(State.id == 2).first()
    obj.name = "New Mexico"
    session.commit()
