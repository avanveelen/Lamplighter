FROM resin/rpi-raspbian:latest

# Install dependencies
RUN apt-get update && apt-get install -y \ 
    tcpdump \
    python3.4 \
    python3-pip

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]