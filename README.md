## 📚 Documentation

Documentation is currently a work in progress.

## 💻 Development

To get started with development, clone the repo and set the following enironment variables:

```bash
export DJANGO_SECRET_KEY=''
export POSTGRES_HOST=''
export POSTGRES_PORT=''
export POSTGRES_DB_NAME=''
export POSTGRES_USER=''
export POSTGRES_PASSWORD=''
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

To set a strict standard, all new pull requests must retain a 100% code coverage. All code should be formatted with the following tools before create a pull request.

### Formatting
```bash
nox -s fix lint
```
