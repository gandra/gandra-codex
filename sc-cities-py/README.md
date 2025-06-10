# sc-cities-py

Small Python client demonstrating how to obtain an access token from `sc-authorization-server` and call the resource servers.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file with `CLIENT_ID` and `CLIENT_SECRET` for the authorization server.

Run:

```bash
python -m sc_cities_py.main
```
