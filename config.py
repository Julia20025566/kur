import configparser
from peewee import *
import os

# Инициализация БД

db = PostgresqlDatabase(
    database=os.getenv("dbName"),
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password")
)


class BaseModel(Model):
    class Meta:
        database = db


