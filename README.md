# Playwright-Github-Actions

Testing the Github actions with a Python project

Executing the project locally:
- Intall the requirements
```bash
.\.venv\Scripts\activate
pip install -r .\requirements.txt
```

- Then, launch the web server
```bash
.\.venv\Scripts\activate
cd cubeit
python -m http.server 8080
```

- And then, execute the tests
```bash
.\.venv\Scripts\activate
pytest -v

# Or
pytest --headed --slowmo=500
```
