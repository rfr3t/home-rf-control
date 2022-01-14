FROM python:2.7-slim-buster

WORKDIR /app
RUN apt-get update
RUN apt-get install -y wget unzip python-usb libusb-1.0.0
#RUN wget https://github.com/rfr3t/home-rf-control/archive/master.zip
#RUN unzip master.zip
#RUN cd home-rf-control-master
COPY homecontrol.py ./
COPY devices ./devices
COPY requirements.txt ./
#RUN git clone https://github.com/rfr3t/home-rf-control.git
#RUN git clone https://github.com/atlas0fd00m/rfcat.git
RUN wget https://github.com/atlas0fd00m/rfcat/archive/master.zip
RUN unzip master.zip
WORKDIR /app/rfcat-master
RUN python -m pip install -e .
WORKDIR /app
RUN python -m pip install -r requirements.txt
CMD ["python", "homecontrol.py"]
