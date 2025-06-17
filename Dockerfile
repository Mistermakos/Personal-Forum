FROM python:3.14-rc-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./

#Installing py packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app/. .

EXPOSE 5000

CMD ["python", "./main.py"]
