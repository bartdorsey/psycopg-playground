import psycopg
from psycopg.rows import class_row
from rich import print, inspect
import os
import dotenv
from pydantic import BaseModel
from datetime import datetime
from psycopg_pool import ConnectionPool


dotenv.load_dotenv()


class Superhero(BaseModel):
    id: int
    name: str
    superpower: str
    archnemesis: str
    age: int
    origin: str
    active: bool
    debut_date: datetime


class DatabaseURLException(Exception):
    pass


class SuperheroDoesNotExist(Exception):
    pass


database_url = os.environ.get("DATABASE_URL")
if database_url is None:
    raise DatabaseURLException("You forgot to define DATABASE_URL in your environment")

pool = ConnectionPool(database_url)


class SuperheroQueries:
    def drop_superheroes_table(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """--sql
                    DROP TABLE IF EXISTS superheroes;
                """
                )

    def create_superheroes_table(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """--sql
                CREATE TABLE
                    IF NOT EXISTS superheroes (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        superpower VARCHAR(50),
                        archnemesis VARCHAR(50),
                        age INTEGER,
                        origin VARCHAR(100),
                        active BOOLEAN DEFAULT TRUE,
                        debut_date DATE
                    );
                """
                )

    def insert_sample_superheroes(self):
        with pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """--sql
                    INSERT INTO
                        superheroes (
                            name,
                            superpower,
                            archnemesis,
                            age,
                            origin,
                            active,
                            debut_date
                        )
                    VALUES
                        (
                            'WonderWoman',
                            'LassoOfTruth',
                            'Ares',
                            3000,
                            'Themyscira',
                            TRUE,
                            '1941-12-01'
                        ),
                        (
                            'SpiderMan',
                            'SpiderSense',
                            'GreenGoblin',
                            28,
                            'New York',
                            TRUE,
                            '1962-08-01'
                        ),
                        (
                            'CaptainAmerica',
                            'ShieldThrowing',
                            'RedSkull',
                            105,
                            'Brooklyn',
                            FALSE,
                            '1941-03-01'
                        ),
                        (
                            'Batman',
                            'MartialArts',
                            'Joker',
                            35,
                            'Gotham',
                            TRUE,
                            '1939-05-01'
                        ),
                        (
                            'Superman',
                            'SuperStrength',
                            'LexLuthor',
                            35,
                            'Krypton',
                            TRUE,
                            '1938-06-01'
                        ),
                        (
                            'Flash',
                            'SuperSpeed',
                            'ReverseFlash',
                            30,
                            'Central City',
                            TRUE,
                            '1956-10-01'
                        ),
                        (
                            'IronMan',
                            'AdvancedTechnology',
                            'Mandarin',
                            48,
                            'New York',
                            FALSE,
                            '1963-03-01'
                        ),
                        (
                            'Thor',
                            'GodOfThunder',
                            'Loki',
                            1500,
                            'Asgard',
                            TRUE,
                            '1962-08-01'
                        ),
                        (
                            'Hulk',
                            'SuperStrength',
                            'Abomination',
                            40,
                            'Dayton',
                            TRUE,
                            '1962-05-01'
                        ),
                        (
                            'BlackWidow',
                            'Espionage',
                            'Taskmaster',
                            35,
                            'Russia',
                            TRUE,
                            '1964-04-01'
                        );
                    """
                )

    def get_all_superheroes(self) -> list[Superhero]:
        with pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Superhero)) as cur:
                result = cur.execute(
                    """--sql
                         SELECT * FROM superheroes;
                    """
                )

                superheroes = result.fetchall()
                return superheroes

    def get_superhero(self, id: int) -> Superhero:
        with pool.connection() as conn:
            with conn.cursor(row_factory=class_row(Superhero)) as cur:
                result = cur.execute(
                    """--sql
                        SELECT * FROM superheroes WHERE id = %s;
                    """,
                    (id,),
                )
                superhero = result.fetchone()
                if superhero is None:
                    raise SuperheroDoesNotExist(f"No superhero with id {id}")
                return superhero


# Tests
queries = SuperheroQueries()
queries.drop_superheroes_table()
queries.create_superheroes_table()
queries.insert_sample_superheroes()
print(queries.get_superhero(100))
