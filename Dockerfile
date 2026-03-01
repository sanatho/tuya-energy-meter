FROM python:3.14-slim

ADD __init__.py .
ADD energy_meter.py .
ADD main.py .
ADD mqtt_client.py .
ADD requirements.txt .
ADD secret.py .
ADD settings.py .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]