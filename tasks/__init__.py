from invoke import Collection

from . import dev
from . import docker

ns = Collection(
    dev,
    docker,
)
