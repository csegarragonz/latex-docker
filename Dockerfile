FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

# Install APT dependencies
RUN apt update && \
    apt upgrade -y && \
    apt install -y \
    gnupg2 \
    libtest-pod-perl \
    wget

# Install TexLive: https://tug.org/texlive/quickinstall.html
ARG TEXLIVE_YEAR
WORKDIR /tmp
RUN wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz && \
    tar xzvf install-tl-unx.tar.gz && \
    cd install-tl-* && \
    perl ./install-tl --no-interaction
ENV PATH="${PATH}:/usr/local/texlive/${TEXLIVE_YEAR}/bin/x86_64-linux"
# Smoke test
RUN latexmk --version

# Prepare entrypoint
WORKDIR /workdir
COPY ./bin/docker_entrypoint.sh /docker_entrypoint.sh
ENTRYPOINT ["/docker_entrypoint.sh"]
