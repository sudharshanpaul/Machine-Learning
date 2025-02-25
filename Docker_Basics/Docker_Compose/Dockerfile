FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP = app.python
ENV FLASK_RUN_HOST = 0.0.0.0
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
