FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 manage.py migrate
RUN python3 manage.py makemigrations

CMD [ "python", "manage.py runserver" ]