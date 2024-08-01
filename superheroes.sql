-- Drop Table
DROP TABLE IF EXISTS superheroes;

-- Create Table
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

-- Insert
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

-- Select all
SELECT
    *
FROM
    superheroes;

-- Update: Change SpiderMan's origin to 'Queens'
UPDATE superheroes
SET
    origin = 'Queens'
WHERE
    name = 'SpiderMan';

-- Select all to see the update
SELECT
    *
FROM
    superheroes;

-- Delete: Remove CaptainAmerica from the table
DELETE FROM superheroes
WHERE
    name = 'CaptainAmerica';

-- Select all to see the changes
SELECT
    *
FROM
    superheroes;

-- Example queries using WHERE, AND, OR, NOT, ORDER BY, GROUP BY
-- WHERE: Select superheroes from 'New York'
SELECT
    *
FROM
    superheroes
WHERE
    origin = 'New York';

-- AND: Select active superheroes with the superpower 'SuperStrength'
SELECT
    *
FROM
    superheroes
WHERE
    superpower = 'SuperStrength'
    AND active = TRUE;

-- OR: Select superheroes who are either from 'Asgard' or 'Krypton'
SELECT
    *
FROM
    superheroes
WHERE
    origin = 'Asgard'
    OR origin = 'Krypton';

-- NOT: Select superheroes who are not active
SELECT
    *
FROM
    superheroes
WHERE
    NOT active;

-- ORDER BY: Select all superheroes ordered by age
SELECT
    *
FROM
    superheroes
ORDER BY
    age;

-- ORDER BY: Select all superheroes ordered by debut date in descending order
SELECT
    *
FROM
    superheroes
ORDER BY
    debut_date DESC;

-- GROUP BY: Count superheroes by origin
SELECT
    origin,
    COUNT(*) AS count
FROM
    superheroes
GROUP BY
    origin;