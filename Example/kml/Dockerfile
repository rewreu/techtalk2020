# the base image dockerfile can be found at sparkbasedocker/Dockerfile
FROM python:3.6

RUN mkdir -p /opt/gpudb/kml/bbx
WORKDIR "/opt/gpudb/kml/bbx"

# Install Required Libraries and Dependencies
ADD requirements.txt  ./
RUN pip3 install -r requirements.txt

# Add Kinetica BlackBox SDK (currently v7.0.11)
ADD bb_runner.sh ./
ADD sdk ./sdk

# Add code and model file
COPY inference_service.py ./
ADD ./model.pkl ./

RUN ["chmod", "+x",  "bb_runner.sh"]
ENTRYPOINT ["/opt/gpudb/kml/bbx/bb_runner.sh"]