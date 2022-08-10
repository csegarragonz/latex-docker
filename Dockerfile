FROM ubuntu:20.04

ARG DEBIAN_FRONTEND=noninteractive

# Proxy settings, eventually remove me
ARG http_proxy=http://proxy-us.intel.com:912
ARG https_proxy=http://proxy-us.intel.com:912

RUN rm -rf /etc/apt/sources.list
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt focal main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt focal-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb-src mirror://mirrors.ubuntu.com/mirrors.txt focal-updates main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt focal-backports main restricted universe multiverse" >> /etc/apt/sources.list
RUN echo "deb mirror://mirrors.ubuntu.com/mirrors.txt focal-security main restricted universe multiverse" >> /etc/apt/sources.list

# Install APT dependencies
RUN apt update && \
    apt upgrade -y && \
    apt install -y \
    gnupg2

# Install MiKTeX
RUN apt-key adv \
    --keyserver hkp://keyserver.ubuntu.com:80 \
    --recv-keys D6BC243565B2087BC3F897C9277A7293F59E4889 && \
    echo "deb http://miktex.org/download/ubuntu bionic universe" | \
    tee /etc/apt/sources.list.d/miktex.list && \
    apt update && \
    apt install miktex
