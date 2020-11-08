FROM python:alpine
WORKDIR /app
COPY app.py /app
RUN pip install flask
ENTRYPOINT ["python", "app.py"]
EXPOSE 5000
