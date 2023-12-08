FROM library/postgres:15.1-alpine

LABEL author="Alex Castillo"
LABEL description="postgres image for django tutorial"
LABEL version="1.0"

# can these be the migations??? how would I create a replica of a large database and fill it with data?
COPY *.sql /docker-entrypoint-initdb.d/

