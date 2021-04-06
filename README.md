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

- Start the server 
```bash
python manage.py runserver 
```

- Linting
```bash
black $(find . -name '*.py')
```

- Architecture:

```bash
- views.py: Handles HTTP only request/response to and fro the server
- services.py: Business domain/logic
- utils.py: Data logic
- models.py: Handles data domain
```