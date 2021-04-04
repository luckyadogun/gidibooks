# gidibooks

- Install Python3.9

- Create and activate virtualenv
```bash
virtualenv env --python=python3.9
source env/bin/activate #unix only
```
- Create a .env file (use `.env.example` as guide)

- Start the database
```bash
docker-compose up -d
```
- Linting
```bash
black $(find . -name '*.py')
```