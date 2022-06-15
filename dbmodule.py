import sqlalchemy as db
from sqlalchemy import Table, Column, Integer, String, MetaData, delete, Float, Numeric, update, Boolean
import pandas as pd
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.sql.expression import func

engine = db.create_engine('sqlite:///SiteDB.db',connect_args={'check_same_thread': False})
meta = MetaData()
conn = engine.connect()
Session = sessionmaker(bind = engine)
sesh = Session()

Wholesale = Table(
    'Wholesale', meta,
        Column('Code', Integer, primary_key = True),
        Column('Title', String),
        Column('Price',Integer),
        Column('Img',String),
        Column('Cat', String),
)
meta.create_all(engine)
