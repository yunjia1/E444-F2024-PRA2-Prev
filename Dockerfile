#specifies the base image
FROM python:3.11-slim

#Set working directory. Susbequent commands executed in this dir
WORKDIR /app

COPY . /app
#install the Python packages listed in requirements.txt using pip3.
RUN pip3 install --no-cache-dir -r requirements.txt

# env variable
ENV FLASK_APP=hello.py
# Application will be listening on port 5000 inside the container
EXPOSE 5000 

# run flask when container launches, make accessible from any IP address
CMD ["flask", "run", "--host=0.0.0.0"]