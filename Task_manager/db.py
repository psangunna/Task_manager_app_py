from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create an engine that connects to the SQLite database located at 'database/tareas.db'
# The 'check_same_thread' argument is set to False to allow the use of the same connection across multiple threads
engine = create_engine('sqlite:///database/tareas.db', connect_args={'check_same_thread': False})

# Create a session factory bound to the engine
# This session factory will be used to create individual sessions that handle transactions with the database
Session = sessionmaker(bind=engine)

# Instantiate a new session from the session factory
# The session is used to interact with the database, perform operations, and manage transactions
session = Session()

# Create a base class for declarative models
# This base class will be used to define models that are mapped to database tables
Base = declarative_base()
