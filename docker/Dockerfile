FROM continuumio/miniconda3

RUN apt-get update && apt-get install build-essential -y
RUN conda update conda && conda install pip

COPY environment.yml /tmp/environment.yml
RUN conda env update -f /tmp/environment.yml -n base && rm /tmp/environment.yml

COPY . /tmp/stactools-pointcloud
RUN cd /tmp/stactools-pointcloud && pip install . && rm -rf /tmp/stactools-pointcloud

ENTRYPOINT [ "python", "-m", "stactools.cli" ]
