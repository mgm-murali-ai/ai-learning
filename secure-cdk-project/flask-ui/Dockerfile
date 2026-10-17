FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV API_URL=YOUR_API_GATEWAY_URL
ENV API_KEY=YOUR_API_KEY

CMD ["python", "app.py"]