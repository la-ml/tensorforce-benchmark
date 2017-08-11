FROM ubuntu:16.04

MAINTAINER reinforce.io <contact@reinforce.io>

# Install dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    libfreetype6-dev \
    libpng12-dev \
    libzmq3-dev \
    pkg-config \
    python \
    python-dev \
    rsync \
    software-properties-common \
    unzip \
    git \
    && \
apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py
 
WORKDIR /
ADD . /

# Add TensorForce dependencies
RUN pip install -r requirements_benchmark.txt

RUN [ -d benchmarks ] || mkdir benchmarks && rm -rf benchmarks/*

ENTRYPOINT ["python", "benchmark.py"]