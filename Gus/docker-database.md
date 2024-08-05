# Database Setup with Docker

```yaml
version: "3"
services:
  django-db:
    container_name: django-db
    restart: always
    image: postgres:13-alpine # use latest official postgres version
    environment:
      POSTGRES_USER: db_username # configure postgres
      POSTGRES_PASSWORD: password
      POSTGRES_DATABASE: polls
    volumes:
      - database-data:/var/lib/postgresql/data/ # persist data even if container shuts down
    expose:
      - 5432
    ports:
      - 5432:5432
    command: -p 5432
    networks:
      - network

volumes:
  database-data: # named volumes can be managed easier using docker-compose
    driver: local
networks:
  network:
    driver: bridge
```

Compose the containers

```bash
docker-compose -f docker-compose.yml up --build -d
```
