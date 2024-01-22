import pytest
import dotenv
import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert
from dotenv import load_dotenv

from jan8.hent_data import Beatles

dotenv.load_dotenv("db.env")
CONNSTR = os.getenv("CONNSTR")

@pytest.fixture()
def engine():
    engine = create_engine(CONNSTR)
    return engine


@pytest.fixture(scope="function")
def tabellen(engine):
    metadata_obj = MetaData()
    tabellen = Table("tabellen",
                     metadata_obj,
                     Column("Id", Integer),
                     Column("Name", String(255)))
    tabellen.drop(engine, checkfirst=True)
    tabellen.create(engine, checkfirst=False)
    with engine.connect() as c:
        stmt = insert(tabellen).values([(1, "John"), (2, "Paul"), (3, "George"), (4, "Ringo")])
        c.execute(stmt)
        c.commit()
    return tabellen

@pytest.fixture(scope="function")
def beatles(engine, tabellen):
    return Beatles(engine, tabellen)


from sqlalchemy import MetaData

@pytest.fixture(scope="function")
def cleanup_tables(engine):
    def _cleanup_tables():
        metadata_obj = MetaData()
        metadata_obj.reflect(bind=engine)

        # Drop "Instrument" table
        if 'SpillerInstrument' in metadata_obj.tables:
            instrument_table = metadata_obj.tables['SpillerInstrument']
            instrument_table.drop(engine, checkfirst=True)

    return _cleanup_tables

