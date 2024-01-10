FROM python:3.11

WORKDIR /app

ENV PYTHONUNBUFFERED=true \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PATH="$POETRY_HOME/bin:$PATH" \
    PYTHONPATH="$PYTHONPATH:/app"

COPY /requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY /api.py /app

ENTRYPOINT ["python", "api.py"]