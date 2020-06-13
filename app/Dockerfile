FROM python:3.7

WORKDIR /opt/app

RUN pip install --user pipenv

COPY Pipfile* ./

RUN python -m pipenv install --system --deploy

COPY app.py .
COPY templates ./templates

ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]