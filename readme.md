# Python Rest-Controller

## Instalação

``` pip install Flask pytz ```

## Endpoint

http://127.0.0.1:5000/current_date?timezone=America/Sao_Paulo

## WSGI

### Linux: gunicorn

``` pip install gunicorn ```

gunicorn rest_controller:app
gunicorn date_controller:app --bind 0.0.0.0:8080 --workers 4
 
### Windows: waitress

``
pip install waitress
waitress-serve --listen=0.0.0.0:8080 date_controller:app
``



## Docker

### Dockerfile

```
FROM python:3.6.1-alpine
RUN pip install flask
COPY app.py /app.py
CMD ["python","app.py"]
```

$ docker image build -t py-rest .
$ docker run -p 5001:5000 -d py-rest

$ docker container logs [container_id]



Enviar para DockerHub

$ docker login
$ docker tag py-rest [dockerhub username]/py-rest
$ docker push [dockerhub username]/py-rest