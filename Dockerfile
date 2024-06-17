FROM docker.io/python:3.11-bullseye
WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app
RUN poetry install

COPY main.py /app
CMD ["poetry", "run", "python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0"]
