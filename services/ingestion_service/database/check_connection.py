from sqlalchemy import text

from services.ingestion_service.database.connection import engine


def check_database_connection() -> None:
    with engine.connect() as connection:
        result = connection.execute(
            text(
                """
                SELECT
                    current_database(),
                    current_user,
                    version()
                """
            )
        )

        row = result.one()

        print(f"Database: {row[0]}")
        print(f"User: {row[1]}")
        print(f"Version: {row[2]}")


if __name__ == "__main__":
    check_database_connection()