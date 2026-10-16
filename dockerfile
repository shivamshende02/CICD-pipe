
FROM python:3.12-slim

WORKDIR /app

COPY requirements-dev.txt .
RUN python -m pip install --no-cache-dir -r requirements-dev.txt

COPY calculator.py test_calculator.py test_integration.py ./

RUN python -m compileall -q calculator.py test_calculator.py test_integration.py

CMD ["python", "-m", "pytest", "-v", "--junitxml=/reports/test-results.xml", "test_calculator.py", "test_integration.py"]
