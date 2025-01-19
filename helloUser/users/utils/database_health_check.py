from django.db import connection
from pathlib import Path


def check_database():
    """Check the status of the database connection."""
    try:
        # Open a connection if it's not already open
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")  # Test query

        # Convert database name and engine to strings, handling WindowsPath
        db_name = connection.settings_dict["NAME"]
        if isinstance(db_name, Path):
            db_name = str(db_name)

        return {
            "status": "Connected",
            "database": db_name,  # Ensure it's a string
            "engine": str(connection.settings_dict["ENGINE"]),  # Ensure engine is a string
        }
    except Exception as e:
        return {
            "status": "Error",
            "error": str(e),
        }
