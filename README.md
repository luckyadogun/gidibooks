# gidibooks

#### DEV ENVIRONMENT:
- Install Python3.9
- Clone this repository
- Create a .env file (use `.env.example` as guide)
- Create and activate virtualenv
```bash
virtualenv env --python=python3.9
source env/bin/activate #unix only
```

- Start the database server
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

#### PROD ENVIRONMENT
- Install Docker & docker-compose
- Clone this repository
- Create a .env file (use `.env.example` as guide)
- Run `docker-compose -f docker-compose.prod.yml up -d --build`


- Architecture:

```bash
- views.py: Handles HTTP only request/response to and fro the server
- services.py: Business domain/logic
- utils.py: Data logic
- models.py: Handles data domain
```

#### Endpoints [working]

- Auth[POST]
```bash
http://127.0.0.1:8000/users/auth/

payload:

{
    "email": "cola@gmail.com",
    "password": "sdoe123"
}

response:

{
    "data": {
        "success": {
            "is_superuser": false,
            "first_name": "Sam",
            "last_name": "Cola",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2021-04-06",
            "email": "cola@gmail.com",
            "user_id": "9b8e9453-e91e-4c6f-a5e8-e8e75989da35"
        }
    }
}
```

- Register[POST]
```bash
http://127.0.0.1:8000/users/register/

payload:

{
    "first_name": "John",
    "last_name": "Doe",
    "email": "jd@gmail.com",
    "password": "dj12345"
}

response:

{
    "data": {
        "success": {
            "is_superuser": false,
            "first_name": "John",
            "last_name": "Doe",
            "is_staff": false,
            "is_active": true,
            "date_joined": "2021-04-07",
            "email": "jd@gmail.com",
            "user_id": "2864e08d-d21b-46be-91c0-794059423997"
        }
    }
}
```

Unfinished Endpoints

- /search&q=book_title: (Query can also be book_id) [GET]
- /mybooks&q=user_id: (UUID not PK) [GET]
- /borrow: (Accepts user_id[uuid] and array of book_ids[uuid]) [POST] 