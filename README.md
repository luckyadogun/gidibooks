# gidibooks

- Install Python3.9
- Activate virtualenv
- Create a .env file (use `.env.example` as guide)
- Start the database
```bash
docker-compose up -d
```
- Linting
```bash
black $(find . -name '*.py')
```