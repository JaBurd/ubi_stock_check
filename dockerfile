FROM python:latest

WORKDIR /usr/app/src

COPY ./app/main.py ./
COPY ./app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "./main.py" ]
