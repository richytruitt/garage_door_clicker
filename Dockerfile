FROM arm32v7/python:3.7.9-buster

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install --no-cache-dir rpi.gpio


CMD ["python3", "./main.py"]