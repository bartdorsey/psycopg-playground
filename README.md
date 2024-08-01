# Psycopg/Postgres playground

This is a quick way to get a postgres database going on your system.

## How to use:

Copy the `.env.sample` file to `.env` and change any of the variables you would like to change in the DATABASE_URL

```docker compose up```

## Connection details

Postgres is running on 15432 on your local machine, 5432 inside the docker container. 

### Connecting from your machine

If you have the psql command line util on your computer you can connect like this (using the credentials from the .env file)

```shell
psql -U <username> -h localhost -p 15432 playground
```

### Connecting from the docker container

If you don't have psql installed, get a shell inside the db container

```shell
docker compose exec db bash
```

Then run psql from there. (No need to specify port as it's 5432 by default inside the container)

```shell
psql -U <username> -h localhost playground
```

### Included samples

To run the samples, create a virtual environment in python and pip install the requirements.txt

```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

#### `queries.py`

This is an example file which creates a superhero table and does some queries using psycopg. It encapsulates all the queryies into a Query class for easy use with something like FastAPI.

#### `superheroes.sql`

This is an example `sql` file which has a bunch of sample queries. You can run it like this if you have psql installed locally

```shell
psql -U <username> -h localhost -p 15432 playground < superheroes.sql
```






