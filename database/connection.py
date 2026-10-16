import sqlite3
from pathlib import Path


DATABASE = Path(__file__).parent / "planner.db"
SCHEMA = Path(__file__).parent / "schema.sql"


def initialise_database():
    connection = sqlite3.connect(DATABASE)

    with open(SCHEMA, "r") as file:
        schema = file.read()

    connection.executescript(schema)
    connection.commit()
    connection.close()


if __name__ == "__main__":
    initialise_database()