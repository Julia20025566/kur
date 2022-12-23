FROM python:3.10.4-alpine

WORKDIR /usr/src/kur

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
COPY ./requrements.txt .
RUN pip install -r requrements.txt

COPY . .

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/kur/entrypoint.sh
RUN chmod +x /usr/src/kur/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/kur/entrypoint.sh"]