FROM python:3.10.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD [ "python", "-m", "app.main" ]

EXPOSE 8000