CREATE DATABASE custom_django;

CREATE USER djangomaster WITH PASSWORD 'dbpass001';

ALTER ROLE djangomaster SET client_encoding TO 'utf8';
ALTER ROLE djangomaster SET default_transaction_isolation TO 'read committed';
ALTER ROLE djangomaster SET timezone TO 'Asia/Kolkata';

GRANT ALL PRIVILEGES ON DATABASE career_capsule TO djangomaster;
