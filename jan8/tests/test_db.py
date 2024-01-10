import pytest
import dotenv
import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert

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


def test_hent_beatle_id_basic(beatles):
    id = beatles.finn_beatle_id("John")
    assert id == 1


def test_hent_beatle_id_injection(beatles):
    beatles.finn_beatle_id("'; DROP TABLE IF EXISTS tabellen; --")
    id = beatles.finn_beatle_id("John")
    assert id == 1
