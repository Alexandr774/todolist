FROM matthewfeickert/docker-python3-ubuntu:latest
ENV PATH /usr/local/bin:$PATH
WORKDIR /todolist
RUN pip install poetry
RUN poetry config virtualenvs.create false
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install
COPY . /todolist
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]