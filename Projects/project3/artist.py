from dataclasses import dataclass
import sqlite3
class No_Artist_Error(Exception):
    """ Custom exception class """
    pass


@dataclass

class Artist:
    key_id=int
    name=str
    email=str

