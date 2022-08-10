from invoke import Collection

from . import docker

ns = Collection(
    docker,
)
