## 📚 Documentation

Documentation is currently a work in progress.

## 💻 Development

To get started with development, you will need to create a Postgres database:
```bash
createdb dinedash                     # Creates PostgreSQL database locally
createuser dinedash -P                # Create a user and prompt for password
```

Next, export the following environment variables with the information you just entered for the database.

```bash
export DJANGO_SECRET_KEY=$(uuidgen)   # Generates a UUID for a secret key
export POSTGRES_HOST='localhost'      # The address of your postgres server
export POSTGRES_PORT='5432'           # Default postgres port 5432
export POSTGRES_DB_NAME='dinedash'    # Database name (created in last step)
export POSTGRES_USER='dinedash'       # Database user (created in last step)
export POSTGRES_PASSWORD=''           # Database password (created in last step)
```

Start a new virtual environment of your choice, or use
```bash
python3 -m venv env/
source env/bin/activate
```

Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements/development.txt
```

## 🧪 Testing

Install dependencies (_note: the testing dependencies are included in the development dependencies_)
```bash
pip install -r requirements/testing.txt
```

### Run unit tests
```bash
nox -s test
```

### Run linting tests
```bash
nox -s lint
```

## 🤝 Contributing

To make future contributions more smooth, all pull requests must retain a 100% code coverage. All code should be tested, formatted, and linted. If all sessions pass, the pull request can be considered for merging.

### Testing, linting, and formatting
```bash
nox         # Fix any errors, broken tests, or missing coverage before submitting a PR
```
