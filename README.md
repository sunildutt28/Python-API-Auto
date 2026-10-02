# Python API Auto

Python API Auto is a lightweight Python project designed to automate API-related tasks such as requests, validations, testing, and workflow automation. It can be used for API smoke testing, contract verification, data-driven testing, or building reusable API automation scripts.

## Features

- Python-based API automation framework
- Support for GET, POST, PUT, DELETE HTTP methods
- Response validation and assertions
- Environment-based configuration
- Easy integration with CI/CD pipelines
- Reusable client and utility modules
- Test automation support with pytest
- SQLAlchemy database support
- Structured logging

## Project Structure

```text
Python-API-Auto/
├── api/
│   ├── __init__.py
│   ├── client.py
│   └── endpoints.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── database/
│   ├── database.py
│   ├── repository.py
│   └── seed.py
├── logs/
├── models/
│   └── user.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_users.py
├── utils/
│   ├── assertions.py
│   └── logger.py
├── .env
├── create_database.py
├── requirements.txt
├── test_config.py
└── README.md
```

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.9 or newer
- pip
- Virtual environment support

## Installation

Clone the repository:

```bash
git clone https://github.com/sunildutt28/Python-API-Auto.git
cd Python-API-Auto
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file with the required settings:

```env
BASE_URL=http://localhost:8000
DATABASE_URL=sqlite:///./app.db
```

The configuration loads environment variables in `config/settings.py`.

## Database Setup

Create the database tables:

```bash
python create_database.py
```

Seed sample data:

```bash
python database/seed.py
```

## Usage

Run the API client:

```bash
python test_config.py
```

Example API client usage:

```python
from api.client import APIClient
from api.endpoints import Endpoints

client = APIClient()

response = client.get(Endpoints.user_by_id(1))
print(response.status_code)
print(response.json())
```

## Testing

Run the test suite with Pytest:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_users.py -q
```

Example test:

```python
def test_get_user(api_client):
    response = api_client.get(Endpoints.user_by_id(1))
    assert_status_code(response, 200)
    user = response.json()
    assert user["id"] == 1
```

## Logging

Logs are saved to the `logs/` directory and output to the console. The logger tracks:

- Request method and URL
- Response status code
- Response time in milliseconds

## Contribution

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a pull request

## License

This project is currently unlicensed.

## Contact

For questions or suggestions, please open an issue in the repository.
