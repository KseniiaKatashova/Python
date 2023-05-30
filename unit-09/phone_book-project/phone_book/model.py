"""This module provides the Phone_book database functionality"""

from pathlib import Path
import configparser
from phone_book import SUCCESS, DB_WRITE_ERROR

DEFAULT_DB_FILE_PATH = Path.home().joinpath("."+Path.home().stem + "_phonebook.json") 

def get_database_path(config_file):
    """Return the current path to the Phone_book database."""
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path):
    """Create the Phone_book database"""
    try:
        db_path.write_text("[]")
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR