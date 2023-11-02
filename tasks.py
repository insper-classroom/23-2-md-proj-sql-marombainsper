import os

from invoke import task
from app.db import get_db, Base, engine
from app.members.model import Member
from sqlalchemy import text

def seed_things():
    classes = [Member]
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
    session = next(get_db())
    things = []
    session.bulk_insert_mappings(cls, things)
    session.commit()
@task
def seed_db(ctx):
    if (
        input("Are you sure wou want to drop all tables and recreate? (y/N) ").lower() == "y"
    ):
        # with engine.begin() as conn:
        #     conn.execute(
        #         text("CREATE TABLE IF NOT EXISTS test")
        #     )
        print("Dropping tables...")
        Base.metadata.drop_all(bind=engine)
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)
        seed_things()
        