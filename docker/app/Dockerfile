FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

EXPOSE 8001/tcp

WORKDIR /code

COPY ../../app /code/app
COPY ../../main.py /code
COPY ../../.env   /code
COPY ../../requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]